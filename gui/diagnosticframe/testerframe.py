from tkinter import *
from customtkinter import *
from tkinter import ttk
class TesterClass:
    def __init__(self, root_frame, diagnostic_frame):
        self.root_frame = root_frame
        self.diagnostic_frame = diagnostic_frame
        self.frame = CTkFrame(self.root_frame)
        self.frame.grid(row=1, column=1)

        title = CTkLabel(self.frame, text="Tester logical address", padx=10,
                      pady=10).grid(row=0, column=0)
        self.textbox = Text(self.frame, width=40, height=10, state='disabled')
        self.textbox.grid(row=0, column=1)
        self.textbox.configure(state='normal')
        text_insert = "You need to run tester scan first." + "\nAfter clicking on tester scan\n" \
                      + "Restart your ECU and wait\n"
        self.textbox.insert('end', text_insert)
        self.textbox.configure(state='disabled')
        self.scan_did_button = CTkButton(self.frame, text="Scan for \nTester logical address", width=20, heigh=3,
                                         command=self.find_tester_logical_address)
        self.scan_did_button.grid(row=0, column=2, padx=10,
                                  pady=10)

    def find_tester_logical_address(self):
        self.textbox.configure(state='normal')

        ip = self.diagnostic_frame.ip_model.ip_address
        min_ecu_address = self.diagnostic_frame.tester_parameters.min_tester_address_textbox.get()
        max_ecu_address = self.diagnostic_frame.tester_parameters.max_tester_address_textbox.get()
        if self.diagnostic_frame.controller:
            self.diagnostic_frame.controller.scan_tester(ip, min_ecu_address, max_ecu_address)
