import subprocess
import optparse
import re


def get_argu():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help = "Interface to change MAC address, example: eth0")
    parser.add_option("-m", "--mac", dest = "new_mac", help = "New MAC address, example: 00:11:22:33:44:55")
    (options, arguments) = parser.parse_args()
    if not (options.interface):
        parser.error("[-] Err0r please indicate a interface or use --help to more information")
    elif not (options.new_mac):
         parser.error("[-] Err0r please indicate the new MAC address or use --help to more information")
    return options

def change_mac(interface, new_mac):
    print("\n[+] Starting MAC_changer.py")
    subprocess.call(["ifconfig", interface, "down"])
    print("[+] Changing MAC address of", interface, "to", new_mac)
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_results = subprocess.check_output(["ifconfig", options.interface])
    mac_adress_search_result = re.search(b"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_results)
    if(mac_adress_search_result):
        return mac_adress_search_result.group(0)
    else:
        print("[-] Cant read the MAC address")

options = get_argu()
change_mac(options.interface, options.new_mac)

current_mac = str(get_current_mac(options.interface), "UTF-8")
print("Current MAC address:", current_mac)

if(current_mac == options.new_mac):
    print("[+] MAC address succefully changed to " + current_mac)
else:
    print("[-] MAC address didnt change (FAILED) ")
    print("[!] To change MAC address you need sudo permission ")