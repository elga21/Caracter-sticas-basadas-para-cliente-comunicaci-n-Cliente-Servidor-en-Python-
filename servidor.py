import socket
import threading

# Lista para almacenar los sockets de los clientes conectados
clientes = []

def manejar_cliente(client_socket, client_address):
    print(f"[Conexión nueva establecida: ] Cliente {client_address} conectado.")
    clientes.append(client_socket)
    conectado = True
    while conectado:
        try:
            msg = client_socket.recv(1024).decode('utf-8')
            if msg:
                print(f"[{client_address}] {msg}")
                client_socket.send("Mensaje recibido por el servidor".encode('utf-8'))
                enviar_a_todos(msg, client_socket)
            else:
                conectado = False
        except:
            conectado = False
            clientes.remove(client_socket)
            client_socket.close()
            print(f"[Desconectado: ] Cliente {client_address} desconectado.")

def enviar_a_todos(mensaje, cliente_actual):
    for cliente in clientes:
        if cliente != cliente_actual:
            try:
                cliente.send(mensaje.encode('utf-8'))
            except:
                clientes.remove(cliente)

def iniciar_servidor():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', 2020))
    server_socket.listen(5)
    print("[Inicializado servidor:] escuchando nuevos sockets:")

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=manejar_cliente, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    iniciar_servidor()
