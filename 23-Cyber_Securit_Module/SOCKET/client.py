import socket

host = "127.0.0.1"
port = 2121

with socket.socket() as soket:
    soket.connect((host,port))
    soket.sendall(b"Hello Cyber")
    data = soket.recv(1024) # Kullanıcıdan gelen veriyide 1024 byte olarak alınmasını sagladık
print(data)
