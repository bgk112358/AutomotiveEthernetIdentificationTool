from tkinter import *
from customtkinter import *
from tkinter import ttk
class DiscoveryClass:
    def __init__(self, root_frame, diagnostic_frame):
        self.root_frame = root_frame
        self.diagnostic_frame = diagnostic_frame
        self.frame = CTkFrame(self.root_frame)
        self.frame.grid(row=3, column=1)

        title = CTkLabel(self.frame, text="DID codes", padx=10,
                      pady=10).grid(row=0, column=0)
        self.textbox = Text(self.frame, width=40, height=10, state='disabled')
        self.textbox.grid(row=0, column=1)
        self.scan_did_button = CTkButton(self.frame, text="Scan DID codes", width=12, heigh=3, command=self.scan_did_ids)
        self.scan_did_button.grid(row=0, column=2, padx=10,
                                  pady=10)

    def scan_did_ids(self):
        min_ecu_address = self.diagnostic_frame.did_parameters.min_did_textbox.get()
        max_ecu_address = self.diagnostic_frame.did_parameters.max_did_textbox.get()
        if self.diagnostic_frame.controller:
            self.diagnostic_frame.controller.scan_did(min_ecu_address, max_ecu_address)
