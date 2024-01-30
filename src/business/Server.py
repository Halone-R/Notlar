import xmlrpc.server 
from src.data.db.DB_Connection import BDConnectionHandler
import bcrypt
from bson import ObjectId
from cryptography.fernet import Fernet
import threading

class ServerThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.daemon = True
        self.server_ip = None
        self.port = None

    def run(self):
        run_server(self.server_ip, self.port)
       

    def set_params(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port

class Server:
    def __init__(self):
        self.__db_handle = BDConnectionHandler()
        self.__db_handle.connect_to_db()
        self.__db_connection = self.__db_handle.get_db_connection()
        self.__collection_name = "Users"

    def register(self, client_name, client_password):
        collection = self.__db_connection.get_collection(self.__collection_name)
        existing_user_count = collection.count_documents({"name": client_name})

        if existing_user_count > 0:
            return "Usuário existente"
        else:
            # Gera um ID único para o usuário
            user_id = str(ObjectId())  # Converte para string para armazenar no MongoDB

            # Hash da senha antes de armazená-la no banco de dados
            hashed_password = bcrypt.hashpw(client_password.encode('utf-8'), bcrypt.gensalt())

            # Inclui o ID no documento do usuário
            message = {"_id": user_id, "name": client_name, "password": hashed_password}
            collection.insert_one(message)
            self.__db_handle.backup_database()

            return f"{client_name} registrado com sucesso."
        
    def has_notes(self, user_id):
        collection = self.__db_connection.get_collection(self.__collection_name)
        existing_user_notes_count = collection.count_documents({"user_id": user_id})
        if existing_user_notes_count > 0:
            return True
        else:
            return False

    def get_user_id(self, name):
        collection = self.__db_connection.get_collection(self.__collection_name)
        result = collection.find_one({"name": name})

        if result:
            return result['_id']
        else:
            return None  # or handle the case when the user is not found
        
    def login(self, client_name, client_password):
        collection = self.__db_connection.get_collection(self.__collection_name)
        user_data = collection.find_one({"name": client_name})

        if user_data:
            hashed_db_password = user_data.get("password", "")
            if hashed_db_password:
                # Verify the hashed password
                if bcrypt.checkpw(client_password.encode('utf-8'), hashed_db_password):
                    return f"Usuário logado com sucesso."
                else:
                    return "Senha incorreta"
            else:
                return "Senha não definida para o usuário"
        else:
            return "Usuário inexistente"
        
    def delete_user(self, user_id):
        collection = self.__db_connection.get_collection(self.__collection_name)
        
        if collection.find({"_id": user_id}):
            if collection.find({"user_id": user_id}):
                collection.delete_many({"user_id":user_id})
            collection.delete_many({"_id":user_id})
            self.__db_handle.backup_database()
            return f"{user_id} deletado com sucesso."
        
        else:
            return "Usuário inexistente"
    
        
    def save_notes(self, note_name, xml_data, user_id):
        collection = self.__db_connection.get_collection(self.__collection_name)

        # Gera uma chave para encriptação
        key = Fernet.generate_key()

        # Cria uma instância do objeto Fernet com a chave gerada
        cipher_suite = Fernet(key)

        # Encripta os dados XML
        encrypted_content = cipher_suite.encrypt(xml_data.encode('utf-8'))

        # Salva a chave usada para encriptação junto com os dados
        message = {"user_id": user_id, "note_name": note_name, "encrypted_content": encrypted_content, "encryption_key": key}
        collection.insert_one(message)
        self.__db_handle.backup_database()

        return f"Nota '{note_name}' salva com sucesso."
    
    def find_notes(self, user_id):
        collection = self.__db_connection.get_collection(self.__collection_name)
        notes = list(collection.find({"user_id": user_id}, {'_id': 0, 'note_name': 1}))
        return [note['note_name'] for note in notes]
    
    def get_note_content(self, user_id, note_name):
        collection = self.__db_connection.get_collection(self.__collection_name)
        note = collection.find_one({"user_id": user_id, "note_name": note_name})
        if note:
            # Recupera a chave usada para encriptação
            key = note["encryption_key"]

            # Cria uma instância do objeto Fernet com a chave
            cipher_suite = Fernet(key)

            # Desencripta os dados
            decrypted_content = cipher_suite.decrypt(note["encrypted_content"]).decode('utf-8')
            return f"Conteúdo da nota '{note_name}': {decrypted_content}"
        else:
            return f"Nota '{note_name}' não encontrada."
        
    
    def delete_note(self, user_id, note_name):
        collection = self.__db_connection.get_collection(self.__collection_name)
        result = collection.delete_one({"user_id": user_id, "note_name": note_name})
        if result.deleted_count > 0:
            self.__db_handle.backup_database()
            return f"Nota '{note_name}' deletada com sucesso."
        
        else:
            return f"Nota '{note_name}' não encontrada."


def run_server(server_ip, port):
    server = xmlrpc.server.SimpleXMLRPCServer((server_ip, port), allow_none=True)
    server.register_instance(Server())
    print(f"Servidor a correr no endereço: {server_ip}, porta:{port}...")
    server.serve_forever()


def start_multi_threaded_server(server_ip, start_port, num_servers, num_threads_per_server):
    for i in range(num_servers):
        port = start_port + i
        for j in range(num_threads_per_server):
            thread = ServerThread()
            thread.set_params(server_ip, port + j) 
            thread.start()
            print(f"Servidor {i+1} iniciado na porta: {port + j}")


start_multi_threaded_server("127.0.0.1", 8000, 3, 4)
