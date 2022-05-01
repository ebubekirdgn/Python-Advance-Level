import scapy.all as scapy

req = scapy.ARP()
print(scapy.ls(req))