import os
from tkinter import *
from customtkinter import *
import gui.mainframe.guiwelcome


class ManageClass:
    def __init__(self, root, main_frame):
        self.interface_frame = main_frame.interface_frame
        self.main_frame = main_frame
        self.frame = CTkFrame(root)
        self.frame.grid(row=2, column=0, sticky='news',padx=10, pady=10,)
        greeting = CTkLabel(self.frame, text="Active project:", padx=10,
                         pady=10).grid(row=0, column=0)
        greeting = CTkLabel(self.frame, text="MyProject", padx=10,
                         pady=10).grid(row=0, column=1)
        self.entry_name = CTkEntry(self.frame)
        self.entry_name.grid(row=1, column=0, padx=10,
                             pady=10)
        button = CTkButton(self.frame, text="Save interface and IP address", command=self.save_all).grid(row=1, column=1, padx=10,
                                      pady=10)
        load = CTkButton(self.frame, text="Load interface and IP address", command=self.load_all).grid(row=2, column=1, padx=10,
                                    pady=10)
        gui.mainframe.guiwelcome.raise_frame(self.frame)

    def save_all(self):
        filename = self.entry_name.get()
        if self.main_frame.controller:
            self.main_frame.controller.save_configuration(filename)

    def load_all(self):
        if self.main_frame.controller:
            self.main_frame.controller.load_configuration()

    def set_attributes(self, res):
        self.main_frame.interface_frame.interface_list.set(res.interface)
        self.main_frame.interface_frame.vlan_active.set(res.vlan_bool)
        if self.main_frame.interface_frame.vlan_active.get():
            self.main_frame.interface_frame.vlan_value.set(res.vlan_id)
        self.main_frame.ip_frame.ip_list.set(res.ip_address)
