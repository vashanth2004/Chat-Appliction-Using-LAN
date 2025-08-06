import socket

# Set up server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))  # Listen on all interfaces, port 12345
server_socket.listen(1)
print("Server is waiting for connection...")

conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024).decode()
    if data.lower() == "exit":
        print("Client has disconnected.")
        break
    print("Client:", data)
    reply = input("Server: ")
    conn.send(reply.encode())

conn.close()
server_socket.close()
