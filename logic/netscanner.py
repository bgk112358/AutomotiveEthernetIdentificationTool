import subprocess

from ifconfigparser import IfconfigParser


def identify_interfaces():
    process = subprocess.run(['ifconfig'], capture_output=True)
    console_output = process.stdout.decode('UTF8')
    interfaces = IfconfigParser(console_output=console_output)
    return interfaces.list_interfaces()


def scan_net(lan_interface, count=4):
    address = 'ff02::1%' + lan_interface
    process = subprocess.Popen(['ping6', '-c 1', address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    network_list = []
    while True:
        output = process.stdout.readline()
        temp = output.strip().split()
        if len(temp) > 5:
            address = temp[3].decode('UTF8')[:-1]
            if address not in network_list and address.startswith("fe80"):
                network_list.append(address)
        return_code = process.poll()
        if return_code is not None:
            break
    return network_list


def scan_address(address):
    if ":" in address:
        process = subprocess.run(['nmap', '-6','-p-', address], capture_output=True)
    return process.stdout.decode('UTF8')
