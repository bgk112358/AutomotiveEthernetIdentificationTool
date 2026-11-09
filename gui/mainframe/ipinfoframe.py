from tkinter import *

import gui.mainframe.guiwelcome
from customtkinter import *


class IPInfoFrame:
    def __init__(self, root, main_frame):
        self.root = root
        self.main_frame = main_frame
        self.frame = CTkFrame(root)
        self.frame.grid(row=3, column=1, sticky='news', padx=10, pady=10, )
        title = CTkLabel(self.frame, text="IP address:", padx=10,
                         pady=10).grid(row=0, column=0)
        self.ip_address = CTkLabel(self.frame, text="", padx=15,
                                   pady=15)
        self.ip_address.grid(row=0, column=1)
        title = CTkLabel(self.frame, text="Active ports:", padx=10,
                         pady=10).grid(row=2, column=0)
        self.textbox = Text(self.frame, width=40, height=10, state='disabled')
        self.textbox.grid(row=2, column=1)
        title = CTkLabel(self.frame, text="Mac address:", padx=10,
                         pady=10).grid(row=1, column=0)
        self.mac_address = CTkLabel(self.frame, text="", padx=10,
                                    pady=10, background="white")
        self.mac_address.grid(row=1, column=1)
        ip_name_label = CTkLabel(self.frame, text="Name of IP address:").grid(
            row=0, column=2)
        self.ip_name = CTkLabel(self.frame, text="", padx=10,
                                pady=10)
        self.ip_name.grid(row=0, column=3)

        ping_label = CTkLabel(self.frame, text="Responds to Ping:", padx=10,
                              pady=10).grid(row=1, column=2)
        self.ping_bool = CTkLabel(self.frame,text="")
        self.ping_bool.grid(row=1, column=3)
        ping_time_label = CTkLabel(self.frame, text="Avg. time for ping response:").grid(row=2,
                                                                                         column=2)
        self.ping_avg = CTkLabel(self.frame,text="", padx=10,
                                 pady=10, )
        self.ping_avg.grid(row=2, column=3)
        gui.mainframe.guiwelcome.raise_frame(self.frame)

    def set_ports(self, result, ip):
        self.main_frame.ip_info_frame.ip_address.configure(text=ip)
        if "0 hosts up" in result:
            self.main_frame.ip_info_frame.textbox.configure(state='normal')
            self.main_frame.ip_info_frame.textbox.delete(1.0, 'end')
            self.main_frame.ip_info_frame.textbox.insert('end', "No active ports")
            self.main_frame.ip_info_frame.textbox.configure(state='disabled')
        else:
            start = result.index("PORT")
            end = result.index("Nmap done")
            fill_text = result[start:end - 4]
            self.main_frame.ip_info_frame.textbox.configure(state='normal')
            self.main_frame.ip_info_frame.textbox.delete(1.0, 'end')
            self.main_frame.ip_info_frame.textbox.insert('end', fill_text)
            self.main_frame.ip_info_frame.textbox.configure(state='disabled')

    def set_rest_info(self, mac_address, it_pings, ping_avg, name_of_ip):
        if mac_address != None:
            self.main_frame.ip_info_frame.mac_address.configure(text=mac_address)
        if it_pings:
            self.main_frame.ip_info_frame.ping_bool.configure(text="True")
            self.main_frame.ip_info_frame.ping_avg.configure(text=ping_avg + " ms")
        else:
            self.main_frame.ip_info_frame.ping_bool.configure(text="False")
            self.main_frame.ip_info_frame.ping_avg.configure(text=0)
        self.main_frame.ip_info_frame.ip_name.configure(text=name_of_ip)
