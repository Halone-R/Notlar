import src.business.Server as Server
import src.presentation.Client as Client

def main():
    mode = input("Digite 'server' para iniciar o servidor ou 'client' para iniciar o cliente: ")
    if mode.lower() == 'server':
        server_ip = input("Digite o endereço IP do servidor (ex: 190.000.0.00): ")
        port = int(input("Digite a porta : "))
        Server.run_server(server_ip, port)
    elif mode.lower() == 'client':
        server_ip = input("Digite o endereço IP do servidor (ex: 190.000.0.00): ")
        port = int(input("Digite a porta : "))
        server_address = f"http://{server_ip}:{port}"
        Client.run_client(server_address)
    else:
        print("Modo inválido. Escolha 'server' ou 'client'.")

if __name__ == "__main__":
    main()