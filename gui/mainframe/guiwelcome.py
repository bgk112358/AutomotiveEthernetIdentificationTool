import customtkinter

from controller.maincontroller import *
from gui.mainframe.interfaceclass import InterfaceClass
from gui.mainframe.ipframe import IPFrame
from gui.mainframe.ipinfoframe import IPInfoFrame
from gui.mainframe.manageframe import ManageClass
from gui.mainframe.scanframe import *
from model.ipmodel import *
from customtkinter import *
def raise_frame(frame):
    frame.tkraise()


class MainWindow:
    def __init__(self):

        self.model = IPModelClass()
        self.root = CTk(className="Automatic tool for DoIP diagnostic")
        self.root.geometry('1250x750')
        path = os.getcwd() + "/gui/car.png"
        p1 = PhotoImage(file=path)
        self.root.iconphoto(False, p1)
        self.rootframe = CTkFrame(self.root)
        self.rootframe.grid(row=0, column=0, sticky='news')

        self.interface_frame = InterfaceClass(self)

        self.ip_info_frame = IPInfoFrame(self.rootframe, self)
        self.ip_frame = IPFrame(self.root, self)
        self.scan_frame = ScanFrame(self.rootframe, self.root, self)
        self.manage_frame = ManageClass(self.rootframe, self)
        self.ip_model = None
        self.controller = MainController(self.model, self)
        raise_frame(self.rootframe)

    def show_info_message(self, name, text):
        messagebox.showinfo(name, text)
