from tkinter import *
from customtkinter import *

class DIDParameterClass:
    def __init__(self, root, diagnostic_frame):
        self.root = root
        self.diagnostic_frame = diagnostic_frame
        self.parameter_frame = CTkFrame(self.root)
        self.parameter_frame.grid(row=3, column=0, sticky='news')
        self.min_label = CTkLabel(self.parameter_frame, text="Minimal value of DID", padx=10,
                               pady=10).grid(row=0, column=0)
        self.min_did_textbox = CTkEntry(self.parameter_frame)
        self.min_did_textbox.grid(row=0, column=1)
        self.max_label = CTkLabel(self.parameter_frame, text="Minimal value of DID", padx=10,
                               pady=10).grid(row=1, column=0)
        self.max_did_textbox = CTkEntry(self.parameter_frame)
        self.max_did_textbox.grid(row=1, column=1)

        self.min_did_textbox.insert('end', "0xf180")
        self.max_did_textbox.insert('end', "0xf200")
