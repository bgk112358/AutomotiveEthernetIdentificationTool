import os
import pickle
from pathlib import Path
from tkinter import filedialog as fd

from doipclient import DoIPClient

import gui.mainframe.guiwelcome as start
from gui.diagnosticframe.guiconnect import ConnectionClass
from logic.netscanner import identify_interfaces, scan_net, scan_address
from logic.networklistener import get_vlan, listen_network, get_more_info
from model.ipmodel import IPModelClass


class MainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def find_vlan(self, interface, vlan_active):
        if interface == "Select interface" or interface == "Nothing":
            self.view.show_info_message("Interface error", "You need to select interface first")
        elif vlan_active is False:
            self.view.show_info_message("Vlan error", "You need to select to enable vlan first")
        else:
            try:
                self.model.vlan_id = get_vlan(interface)
                self.view.interface_frame.set_vlan(self.model.vlan_id)
            except StopIteration:
                self.view.show_info_message("Vlan error",
                                            "No packets with vlan were found in timeout on this interface")

    def find_interfaces(self):
        interfaces = identify_interfaces()
        self.view.interface_frame.set_option_menu(interfaces)

    def call_ping(self, interface):
        if interface == "Select interface" or interface == "Nothing":
            self.view.show_info_message("Interface error", "You need to select interface first")
        else:
            result = scan_net(interface)
            if len(result) != 0:
                self.view.scan_frame.set_ip_option(result)
                self.model.interface = interface

    def find_vehicle_announcement(self, interface):
        if interface == "Select interface" or interface == "Nothing":
            self.view.show_info_message("Interface error", "You need to select interface first")
        else:
            address, announcement = DoIPClient.await_vehicle_announcement(ipv6=True, timeout=10)
            convert = [str(address[0])]
            self.view.scan_frame.set_ip_option(convert)
            self.model.interface = interface

    def scan_network(self, interface):
        if interface == "Select interface" or interface == "Nothing":
            self.view.show_info_message("Interface error", "You need to select interface first")
        else:
            try:
                ret_addresses = listen_network(interface)
                self.view.scan_frame.set_ip_option(ret_addresses)
                self.model.interface = interface
            except StopIteration:
                self.view.show_info_message("IP error", "No packets were found in timeout on this interface")

    def get_info_about_ip_address(self, ip):
        if ip == "Select IP address" or ip == "Nothing":
            self.view.show_info_message("IP error", "You need to select ip address first")
        else:
            result = scan_address(ip)
            self.view.ip_info_frame.set_ports(result, ip)
            interface = self.view.interface_frame.interface_list.get()
            self.model.ip_address = ip
            self.model.interface = interface
            mac_address, it_pings, ping_avg, name_of_ip = get_more_info(ip, interface=interface)
            self.view.ip_info_frame.set_rest_info(mac_address, it_pings, ping_avg, name_of_ip)
            self.model = IPModelClass(ip, interface=interface, mac_address=mac_address,
                                      ping_response=it_pings, ping_response_time=ping_avg, ip_name=name_of_ip)

    def connect_to_ip(self, ip):
        if ip == "Select IP address":
            self.view.show_info_message("IP error", "You need to select ip address first")
        else:
            is_doip = False
            try:
                doipclient = DoIPClient(ip, 0x0000, activation_type=None)
                doipclient.close()
                is_doip = True
            except:
                self.view.show_info_message("Error", "Couldn't connect probably not an ECU")
            if is_doip is not True:
                if self.model.ip_address != ip:
                    self.model = IPModelClass(ip_address=ip,interface=self.view.interface_frame.interface_list.get(),ecu_bool=True)
                    next_frame = ConnectionClass(self.view, self.model)
                    start.raise_frame(next_frame.rootframe)
                else:
                    next_frame = ConnectionClass(self.view, self.model)
                    start.raise_frame(next_frame.rootframe)

    def save_configuration(self, filename):
        if filename != "":
            name = "saves/" + filename
        else:
            name = "saves/" + "configuration"
        self.model.ip_address = self.view.ip_frame.ip_list.get()
        self.model.interface = self.view.interface_frame.interface_list.get()
        if os.path.exists(name):
            os.remove(name)
        file_handler = open(name, 'wb')
        pickle.dump(self.model, file_handler)
        file_handler.close()

    def load_configuration(self):
        path = Path('.')
        savepath = path / 'saves'
        final = savepath.resolve()
        name = fd.askopenfilename(initialdir=str(final))
        filehandler = open(name, 'rb')
        unpickler = pickle.Unpickler(filehandler)
        res = unpickler.load()
        self.view.manage_frame.set_attributes(res)
