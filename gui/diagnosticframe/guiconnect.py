from tkinter import *
from tkinter import messagebox

from controller.diagnosticcontroller import DiagnosticController
from gui.diagnosticframe.didframe import DiscoveryClass
from gui.diagnosticframe.didparametersframe import DIDParameterClass
from gui.diagnosticframe.dtcframe import DTCClass
from gui.diagnosticframe.exportframe import ExportClass
from gui.diagnosticframe.testerframe import TesterClass
from gui.diagnosticframe.testerparametersframe import TesterParametersClass
from model.ecumodel import ECUModelClass
from customtkinter import *

def raise_frame(frame):
    frame.tkraise()


class ConnectionClass:
    def __init__(self, previouse_window, ip_model):
        self.model = ECUModelClass(ip_address=ip_model.ip_address)
        self.root = previouse_window.root
        self.ip_model = ip_model
        self.rootframe = CTkFrame(self.root)

        self.rootframe.grid(row=0, column=0, sticky='news')
        greeting = CTkLabel(self.rootframe, text="ECU connected",
                         padx=10, pady=10, text_font=("Arial", 24)).grid(row=0, column=1)

        self.tester = TesterClass(self.rootframe, self)
        self.tester_parameters = TesterParametersClass(self.rootframe, self)
        self.did_parameters = DIDParameterClass(self.rootframe, self)
        self.discovery = DiscoveryClass(self.rootframe, self)
        self.dtc = DTCClass(self.rootframe, self)
        self.export = ExportClass(self.rootframe, previouse_window.rootframe, self)
        self.controller = DiagnosticController(self.model, self)

    def show_info_message(self, name, text):
        messagebox.showinfo(name, text)
