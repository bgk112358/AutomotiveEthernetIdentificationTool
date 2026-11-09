from tkinter import *
from customtkinter import *
from tkinter import ttk
class DTCClass:
    def __init__(self, root_frame, diagnostic_frame):
        self.root_frame = root_frame
        self.diagnostic_frame = diagnostic_frame
        self.frame = CTkFrame(self.root_frame)
        self.frame.grid(row=2, column=1, padx=10, pady=10)

        title = CTkLabel(self.frame, text="DTC codes from ECU ", padx=10,
                      pady=10).grid(row=0, column=0)
        self.textbox = Text(self.frame, width=50, height=10, state='disabled')
        self.textbox.grid(row=0, column=1)
        self.scan_did_button = CTkButton(self.frame, text="Scan DTC codes", width=20, heigh=3, command=self.find_dtc_codes)
        self.scan_did_button.grid(row=0, column=2, padx=10,
                                  pady=10)

    def find_dtc_codes(self):
        if self.diagnostic_frame.controller:
            self.diagnostic_frame.controller.scan_dtc()
