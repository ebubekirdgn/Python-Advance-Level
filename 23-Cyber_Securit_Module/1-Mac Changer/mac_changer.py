from re import sub
import subprocess
import optparse as opt
import re


def get_user_input():
    parse_object = opt.OptionParser()
    parse_object.add_option("-i", "--ipaddress",dest="interface", help="Enter IP Address")
    return parse_object.parse_args()


def change_mac_address(user_interface, user_mac_address):
    subprocess.call(["ifconfig", user_interface, "down"])
    subprocess.call(["ifconfig", user_interface, "hw", user_mac_address])
    subprocess.call(["ifconfig", user_interface, "up"])


def control_new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig", interface])
    new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig))
    if new_mac_address:
        return new_mac_address.group(0)
    else:
        return None


print("My Mac Changer Started!")

(user_input, arguments) = get_user_input()
change_mac_address(user_input.interface, user_input.mac_address)
finalized_mac = control_new_mac(str(user_input.interface))

if finalized_mac == user_input.mac_address:
    print("Success!")
else:
    print("Error!")
