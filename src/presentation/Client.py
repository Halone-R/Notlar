import xmlrpc.client


class Client:
    def __init__(self, server_address):
        self.server = xmlrpc.client.ServerProxy(server_address)

    def register(self, name, password):
        return self.server.register(name, password)
    
    def delete_note(self, name, note_name):
        return self.server.delete_note(name, note_name)
    
    def read_note(self, name, note_name):
        return self.server.get_note_content(name, note_name)
    
    def save_note(self, note_name, message, name):
        return self.server.save_notes(note_name, message, name)

    def list_notes(self, name):
        return self.server.find_notes(name)
    
    def find_message(self,name):
        return self.server.find_message(name)
    
    def login(self, name, password):
        return self.server.login(name,password)
    
    def delete_user(self, name):
        return self.server.delete_user(name)
    
    def get_user_id(self, name):
        return self.server.get_user_id(name)
    
    def has_notes(self, user_id):
        return self.server.has_notes(user_id)
    

def run_client(server_address):
    client = Client(server_address)
    while True:
        
        print("\n___Bem vindo ao Notlar___\n")
        print("\n______MENU______\n")
        print(" --------------")
        print("| Registar (r) |")
        print("| Entrar   (e) |")
        print("| Sair     (s) |")
        print(" --------------\n")

        choice = input("Escolha uma opção:")

        if choice == "r":
            name = input("Username: ")
            password = input("Password: ")
            print(client.register(name,password))

        elif choice == "e":
            name = input("Username: ")
            password = input("Password: ")
            user_id = client.get_user_id(name)
            print(client.login(name,password))
            if (client.login(name, password) == "Usuário inexistente" or client.login(name, password) == "Senha incorreta"):
                continue
            else:
                logged_in = True
                while logged_in :
                    print("\n____________MENU____________\n")
                    print(" ---------------------------")
                    print("| Escrever uma nota     (w) |")
                    print("| Ler uma nota          (r) |")
                    print("| Apagar uma nota      (dn) |")
                    print("| Apagar Usuário       (du) |")
                    print("| Sair                  (s) |")
                    print(" ---------------------------\n")
                    choice = input("Escolha uma opção:")
                    if choice == "w":
                        note_name = input("\nNome da nota: ")
                        message = input("Conteúdo:")
                        client.save_note(note_name, message, user_id)
    
                    elif choice == "r":
                        notes = client.list_notes(user_id)
                        if(client.has_notes(user_id) == False):
                            print("\nSem notas.")
                        else:
                            print("\nNotas disponíveis:")
                            for note in notes:
                                print(f"- {note}")

                            note_name = input("\nEscolha uma nota para ler: ")
                            content = client.read_note(user_id, note_name)
                            print(content)

                    elif choice == "dn":
                        notes = client.list_notes(user_id)
                        if(client.has_notes(user_id) == False):
                            print("\nVocê não tem nenhuma nota.")
                        else:
                            print("\nNotas disponíveis:")
                            for note in notes:
                                print(f"- {note}")

                            note_name = input("\nEscolha uma nota para apagar: ")
                            result = client.delete_note(user_id, note_name)
                            print(result)

                    elif choice == "du":
                        client.delete_user(client.get_user_id(name))
                        logged_in = False

                    elif choice == "s":
                        logged_in = False

                        
                    else:
                        print("\nEnter a valid option")
                

        elif choice == "s":
            break
        else:
            print("\nInvalid Option\nPlease enter a valid option.")
            print("")
