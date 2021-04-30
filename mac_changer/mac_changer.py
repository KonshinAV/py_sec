#!/usr/bin/env python3

import subprocess
import optparse

def get_arguments():
    pars = optparse.OptionParser()
    pars.add_option('-i', '--interface', dest='interface', help="Interface to change MAC address")
    pars.add_option('-m', '--mac', dest='new_mac', help="New MAC address")
    return pars.parse_args()

def change_mac (interface, new_mac):
    print(f"[+] Changing MAC address for interface {interface} to {new_mac}")
    # subprocess.call(["ifconfig", interface, "down"])
    # subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    # subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)