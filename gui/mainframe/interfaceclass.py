from tkinter import *
from tkinter import messagebox

import gui.mainframe.guiwelcome
from customtkinter import *
from tkinter import ttk

class InterfaceClass:
    def __init__(self, main_frame):
        self.main_frame = main_frame
        self.frame = CTkFrame(self.main_frame.rootframe)
        self.frame.grid(row=1, column=0, sticky='news',padx=10, pady=10,)
        self.greeting = CTkLabel(self.frame, text="Interface name", padx=10,
                                 pady=10).grid(row=0, column=0, padx=10, pady=10)
        self.interface_list = StringVar()
        self.interface_list.set("wlp1s0")
        self.optionIP = ttk.OptionMenu(self.frame, self.interface_list, "Nothing")
        self.optionIP.grid(row=0, column=1, padx=10, pady=10)
        self.vlan_active = BooleanVar()
        self.vlan_check = CTkCheckBox(self.frame, variable=self.vlan_active, onvalue=True, offvalue=False,
                                      text="Virtual LAN").grid(row=1, column=0,padx=10, pady=10,)
        self.small_frame = CTkFrame(self.frame)
        self.small_frame.grid(row=1, column=1, sticky='news')
        self.vlan_label = CTkLabel(self.small_frame, text="VLAN id").grid(row=0, column=0,padx=10, pady=10)
        self.vlan_value = IntVar(value=0)
        self.number_box = CTkEntry(self.small_frame, textvariable=self.vlan_value).grid(row=0, column=1)
        self.find_vlan_button = CTkButton(self.frame, text="Find VLAN",
                                          command=lambda: self.fill_vlan(self.interface_list.get(),
                                                                         self.vlan_active.get()))
        self.find_vlan_button.grid(row=2, column=1, padx=10, pady=10)
        self.update_interface_button = CTkButton(self.frame, text="Update Interface",
                                                 command=self.fill_interfaces).grid(
            row=2, column=0, padx=10, pady=10)
        gui.mainframe.guiwelcome.raise_frame(self.frame)

    def fill_vlan(self, interface, vlan_active):
        if self.main_frame.controller:
            self.main_frame.controller.find_vlan(interface, vlan_active)

    def fill_interfaces(self):
        if self.main_frame.controller:
            self.main_frame.controller.find_interfaces()

    def set_vlan(self, vlan_id):
        self.vlan_value.set(vlan_id)

    def set_option_menu(self, interfaces):
        self.optionIP.destroy()
        self.optionIP = ttk.OptionMenu(self.frame, self.interface_list,interfaces[0], *interfaces).grid(row=0, column=1)
