#!/usr/bin/env python3

import subprocess
import optparse
import re

def get_arguments():
    pars = optparse.OptionParser()
    pars.add_option('-i', '--interface', dest='interface', help="Interface to change MAC address")
    pars.add_option('-m', '--mac', dest='new_mac', help="New MAC address")
    (options, arguments) = pars.parse_args()
    if not options.interface:
        pars.error("[-] Please specify an interface, use --help for more information")
    elif not options.new_mac:
        pars.error("[-] Please specify an mac address, use --help for more information")
    return options
def change_mac (interface, new_mac):
    print(f"[+] Changing MAC address for interface {interface} to {new_mac}")
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    # for i in str(ifconfig_result).split("\\n"): print(i)
    # \w\w:\w\w:\w\w:\w\w:\w\w:\w\w - re for find mac
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read mac address")

options = get_arguments()
current_mac = get_current_mac(options.interface) # 00:15:5d:1f:64:14
print (f"Current MAC = {current_mac}")

current_mac = get_current_mac(options.interface)
change_mac(options.interface, options.new_mac)
if current_mac == options.new_mac:
    print(f"[+] MAC address was successfully changed to {current_mac}")
else:
    print(f"[+] MAC address didn't changed")
