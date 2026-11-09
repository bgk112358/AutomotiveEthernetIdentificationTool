from tkinter import *
from customtkinter import *
import gui.mainframe.guiwelcome


class ExportClass:
    def __init__(self, rootframe, mainframe, diagnostic_frame):
        self.rootframe = rootframe
        self.mainframe = mainframe
        self.diagnostic_frame = diagnostic_frame
        self.export_frame = CTkFrame(self.rootframe)
        self.export_frame.grid(row=4, column=1, padx=10,pady=10,sticky='news')
        button = CTkButton(self.export_frame, text="Export results", width=25, heigh=5, command=self.create_pdf).grid(
            row=0, column=2)
        button = CTkButton(self.export_frame, text="Get back to Main window", width=20, heigh=5,
                        command=self.return_to_main) \
            .grid(row=0, column=1, padx=10, pady=10)

    def return_to_main(self):
        gui.mainframe.guiwelcome.raise_frame(self.mainframe)#
    def create_pdf(self):
        if self.diagnostic_frame.controller is not None:
            self.diagnostic_frame.controller.generate_pdf()
