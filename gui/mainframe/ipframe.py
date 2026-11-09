import subprocess
from tkinter import *
import tkinter.ttk
from tkinter import ttk

import gui.mainframe.guiwelcome
from customtkinter import *

class IPFrame:
    def __init__(self, root, main_frame):
        self.root = root
        self.main_frame = main_frame
        self.frame = CTkFrame(self.main_frame.rootframe)
        self.frame.grid(row=2, column=1, sticky='news',padx=10, pady=10,)
        greeting = CTkLabel(self.frame, text="IP address", padx=10,
                         pady=10).grid(row=0, column=0)
        self.ip_list = StringVar()
        self.ip_list.set("Select IP address")
        self.optionIP = ttk.OptionMenu(self.frame, self.ip_list, "Nothing")
        self.optionIP.grid(
            row=0, column=1, padx=10, pady=10)
        buttonConnect = CTkButton(self.frame, text="Connect to this IP address", width=25, height=2,
                               command=self.connect_ip_address).grid(
            row=0, column=3, padx=10, pady=30)
        button_info_ip = CTkButton(self.frame, text="Get info about this IP address", width=25, height=2,
                                command=self.get_info_ip_address).grid(
            row=0, column=2, padx=10, pady=30)
        gui.mainframe.guiwelcome.raise_frame(self.frame)

    def get_info_ip_address(self):
        ip = self.main_frame.ip_frame.ip_list.get()
        if self.main_frame.controller:
            self.main_frame.controller.get_info_about_ip_address(ip)

    def connect_ip_address(self):
        ip = self.main_frame.ip_frame.ip_list.get()
        if self.main_frame.controller:
            self.main_frame.controller.connect_to_ip(ip)
