from tkinter import *
from tkinter import messagebox, ttk
import tkinter.ttk
import gui.mainframe.guiwelcome
from customtkinter import *

class ScanFrame:
    def __init__(self, rootframe, root, main_frame):
        greeting = CTkLabel(rootframe, text="Welcome in tool for Automatic\n identification of Automotive Ethernet",
                         padx=10,
                         pady=10, font=("Arial", 20), fg_color="white").grid(row=0, column=0,columnspan=2)

        self.frame = CTkFrame(rootframe)
        self.frame.grid(row=1, column=1, padx=10, pady=10,sticky='news')
        self.main_frame = main_frame
        connectping = CTkLabel(self.frame, text="Scan IP address\n on lan using ping", padx=10, pady=10,
                            fg_color="white").grid(
            row=0, column=0)
        connectdoip = CTkLabel(self.frame, text="Scan IP using DoIP announcement message,\n"
                                             "Click this button and power cycle your ECU.\n"
                                             "If announcement is not received in 20 seconds,\n connection is unsuccesful.",
                            padx=10, pady=10, fg_color="white").grid(
            row=0, column=1)
        connectnetworklistner = CTkLabel(self.frame, text="Try to connect to your ECU\n by using IP addresses\n"
                                                       "that are active on local network", fg_color="white").grid(
            row=0,
            column=2)

        buttonping = CTkButton(self.frame, text="Ping scan",
                            command=self.call_ping).grid(row=1,
                                                         column=0,
                                                         padx=10,
                                                         pady=10)
        buttonDoIP = CTkButton(self.frame, text="DoIP scan",
                            command=self.doip_announcement).grid(row=1,
                                                                 column=1,
                                                                 padx=10,
                                                                 pady=10)
        buttonNewtork = CTkButton(self.frame, text="Network scan",
                               command=self.scan_network).grid(row=1,
                                                               column=2,
                                                               padx=10,
                                                               pady=10)
        gui.mainframe.guiwelcome.raise_frame(self.frame)

    def call_ping(self):
        interface = self.main_frame.interface_frame.interface_list.get()
        if self.main_frame.controller:
            self.main_frame.controller.call_ping(interface)

    def scan_network(self):

        interface = self.main_frame.interface_frame.interface_list.get()
        if self.main_frame.controller:
            self.main_frame.controller.scan_network(interface)

    def doip_announcement(self):
        interface = self.main_frame.interface_frame.interface_list.get()
        if self.main_frame.controller:
            self.main_frame.controller.find_vehicle_announcement(interface)

    def set_ip_option(self, list_of_ips):
        self.main_frame.ip_frame.optionIP.destroy()
        self.main_frame.ip_frame.optionIP = ttk.OptionMenu(self.main_frame.ip_frame.frame, self.main_frame.ip_frame.ip_list,list_of_ips[0], *list_of_ips).grid(
            row=0, column=1, padx=10, pady=10)
