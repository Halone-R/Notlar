import xmlrpc.server



class Server:
    def __init__(self):
        self.clients = []

    def register(self, client_name):
        #Regista um novo cliente """
        if client_name not in self.clients:
            self.clients.append(client_name)
            return f"{client_name} registado com sucesso."
        else:
            return f"{client_name} já está registado."



def run_server(server_ip, port):
    server = xmlrpc.server.SimpleXMLRPCServer((server_ip, port), allow_none=True)
    print(f"Servidor a correr no endereço {server_ip}:{port}...")
    server.serve_forever()

def main():
    mode = input("Digite 'server' para iniciar o servidor")
    if mode.lower() == 'server':
        server_ip = input("Digite o endereço IP do servidor (ex: 190.000.0.00): ")
        port = int(input("Digite a porta : "))
        Server.run_server(server_ip, port)
    
