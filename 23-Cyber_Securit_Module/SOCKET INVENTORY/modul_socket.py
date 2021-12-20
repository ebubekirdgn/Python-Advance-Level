import socket

port_list = []
banner_list = []

file = open("SOCKET INVENTORY/ip.txt","r")
ips = file.read()
file.close()

for ip in ips.splitlines():
    print(ip)
    for port in range(1,25):
        try:
            soket = socket.socket()
            soket.connect((str(ip),int(port)))
            banner = soket.recv(1024)
            banner_list.append(str(banner))
            port_list.append(str(port))
            soket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("This system can be linux or network device")
                log = str(ip) + "\n"
                file = open("linux.txt","a")
                file.write(log)
                file.close()                
        except:
            pass
        
print(port_list)
print(banner_list)
        
    