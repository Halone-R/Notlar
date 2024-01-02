import Server
import Client
from Mongodb_handler import run




def main():
    print("Bem vindo!")
    server_ip = input("Digite o endereço IP do servidor (ex: 190.000.0.00): ")
    port = int(input("Digite a porta : "))
    run()
    server_address = f"http://{server_ip}:{port}"
    Client.run_client(server_address)



if __name__ == "__main__":
    main()
