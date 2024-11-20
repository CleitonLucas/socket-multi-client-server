import socket
import uuid

SOCKET_PATH = "/tmp/socket_server"

def start_client():
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(SOCKET_PATH)

    # Envia um identificador único para o servidor
    client_id = str(uuid.uuid4())
    client.sendall(client_id.encode())
    print(f"Conectado ao servidor com o ID: {client_id}")

    try:
        while True:
            # Lê entrada do usuário
            message = input("Digite sua mensagem: ")
            if message.lower() == 'sair':
                print("Encerrando cliente...")
                break
            client.sendall(message.encode('utf-8'))
    except KeyboardInterrupt:
        print("Cliente encerrado pelo usuário.")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()
