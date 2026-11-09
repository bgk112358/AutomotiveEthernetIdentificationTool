import subprocess

import pyshark


def listen_network(interface):
    address_captured = []
    try:
        capture = pyshark.LiveCapture(interface=interface)
        for packet in capture.sniff_continuously(packet_count=20):
            address = None
            if "IPV6" in packet:
                address = packet["IPV6"].src
            elif "IP" in packet:
                address = packet["IP"].src
            else:
                continue
            if address not in address_captured:
                address_captured.append(address)
        return address_captured
    except:
        raise StopIteration


def get_vlan(interface):
    capture = pyshark.LiveCapture(interface=interface)
    try:
        for packet in capture.sniff_continuously(packet_count=20):
            if "VLAN" in packet:
                return packet['VLAN'].id
    except:
        raise StopIteration


def get_more_info(ip, interface):
    capture = pyshark.LiveCapture(interface=interface)
    it_pings = False
    ping_avg = 0
    process = subprocess.Popen(['ping6', '-c 4', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    mac_address = None
    for packet in capture.sniff_continuously(packet_count=5):
        if "IPV6" in packet:
            address = packet["IPV6"].src
            if address in ip:
                mac_address = packet[0].src_resolved
            else:
                mac_address = packet[0].dst_resolved
    output = process.stdout.readline()
    temp = output.strip().split()
    while len(temp) > 0 or output.decode('UTF8') == "\n":
        output = process.stdout.readline()
        if output.decode('UTF8') != "\n":
            temp = output.strip().split()
            avg = temp[1].decode('UTF8')
            if "avg" in avg:
                ping_responses = temp[3].decode('UTF8')
                split_ping = ping_responses.split('/')
                ping_avg = split_ping[1]
                it_pings = True
                break
    strip_ip = ip
    if '%' in ip:
        result = ip.find('%')
        strip_ip = ip[:result]
    process = subprocess.Popen(['nslookup', strip_ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.stdout.readline()
    temp = output.strip().split()
    name_of_ip = temp[3]
    return mac_address, it_pings, ping_avg, name_of_ip
