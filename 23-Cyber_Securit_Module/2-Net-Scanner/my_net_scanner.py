from socket import timeout
import scapy.all as scapy
import optparse as opt


# 1- Arp Request
# 2- Broadcast
# 3- Response


def get_user_input():
    parse_object = opt.OptionParser()
    parse_object.add_option("-i","--ipaddress",dest="ip_address",help="interface to change")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter Ip Address")
    return user_input
    

def scan_my_network(ip):
    arp_request_packet = scapy.ARP(pdst=ip)
    #scapy.ls(scapy.ARP())
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())
    combined_packet = broadcast_packet / arp_request_packet
    (answered_list , unanswered_list ) = scapy.srp(combined_packet,timeout=1)
    #print(list(answered_list))
    answered_list.summary()


user_ip_address = get_user_input()
scan_my_network(user_ip_address.ip_address)