import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("192.168.1.131", 9996)
server_socket.bind(server_address)
server_socket.listen(5)

print("Server listening on {}:{}".format(*server_address))

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    print("Connection from", client_address)

    audio_data = b''
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        audio_data += chunk

    timestamp = datetime.now().strftime("%Y/%m/%d-%H:%M:%S")
    client_id = str(client_address[0]) + '_' + str(client_address[1])
    file_name = f'received_audio_{client_id}_{timestamp}.wav'

    with open(file_name, 'wb') as file:
        file.write(audio_data)

    print(f"Audio file '{file_name}' saved")

    # Close the client socket
    client_socket.close()
