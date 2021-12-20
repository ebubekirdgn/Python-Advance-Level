from ctypes import DEFAULT_MODE
import  socket

host = "127.0.0.1"
port = 2121

with socket.socket() as soket:
    soket.bind((host,port))
    soket.listen()
    conn, addr = soket.accept()
    with conn:
        print("Baglanti yapildi : ", addr)
        while True:
            data = conn.recv(1024) # baglanti adresimizden sürekli olarak 1024 byte bilgi alınmasını saglayacagız.
            if not data:
                break
            conn.sendall(data)