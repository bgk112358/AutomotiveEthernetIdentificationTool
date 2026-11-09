from tkinter import *
from customtkinter import *


class TesterParametersClass:
    def __init__(self, root, diagnostic_frame):
        self.root = root
        self.diagnostic_frame = diagnostic_frame
        self.parameter_frame = CTkFrame(self.root)
        self.parameter_frame.grid(row=1, column=0, sticky='news')
        self.min_label = CTkLabel(self.parameter_frame, text="Minimal value of tester logical address", padx=10,
                                  pady=10).grid(row=0, column=0)
        self.min_tester_address_textbox = CTkEntry(self.parameter_frame)
        self.min_tester_address_textbox.grid(row=0, column=1)
        self.max_label = CTkLabel(self.parameter_frame, text="Minimal value of tester logical address", padx=10,
                                  pady=10).grid(row=1, column=0)
        self.max_tester_address_textbox = CTkEntry(self.parameter_frame)
        self.max_tester_address_textbox.grid(row=1, column=1)
        self.min_tester_address_textbox.insert('end', "0x0E77")
        self.max_tester_address_textbox.insert('end', "0x0E87")
        # button = Button(self.parameter_frame, text="Export to PDF", width=10, heigh=5).grid(
        #   row=0, column=1)
