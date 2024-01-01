import xmlrpc.client
from Mongodb_handler import *
from Encrypt import *
db_url = 'mongodb+srv://saranogueira1:password1990@cluster0.36qrg1i.mongodb.net/' #change when connecting to a different database
db_name = 'messages'
collection_name = 'xmlrpc_messages'
collection_name_u = 'users'



class Client:
    def __init__(self, server_address):\
        self.server = xmlrpc.client.ServerProxy(server_address)

    def register(self, name, password):
        db = connect_to_mongodb(db_url, db_name)
        save_users(db, collection_name_u, name, password)
        return self.server.register(name)

    def send_message(self,message,name):
        # Connect to MongoDB
        db = connect_to_mongodb(db_url, db_name)
        
        # Save XML-RPC message to MongoDB
        save_notes(db, collection_name, message, name)
    
    def find_message(self,name):
        db = connect_to_mongodb(db_url, db_name)
        notes = find_notes(db, collection_name, name)
        
def encrypt(content):
    key = generate_key()
    save_key(key)
    loaded_key = load_key()
    encrypt_content = encrypt_message(content, loaded_key)
    return encrypt_content
    


def run_client(server_address):
    client = Client(server_address)
    name = input("Username: ")
    password = encrypt(input("Password: "))
    print(client.register(name,password))
    choice = input ("MENU write(w)| retrieve(r): ")
    if choice == "w":
        isTrue = True
        while isTrue:
            message = input(f"Write a note - press q to quit: ")
            if message == "q":
                isTrue = False
            else:
                client.send_message(encrypt(message), name)
            
    elif choice == "r":
        client.find_message(name)
    else:
        print("Enter a valid option")

    


