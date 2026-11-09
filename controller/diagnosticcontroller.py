from doipclient import DoIPClient

from logic.hexcheck import check_hex_numbers
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors


class DiagnosticController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def scan_tester(self, ip, min_ecu_address, max_ecu_address):
        min_ecu_address, max_ecu_address = check_hex_numbers(min_ecu_address, max_ecu_address,
                                                             view=self.view)
        if min_ecu_address is not None and max_ecu_address is not None:
            if min_ecu_address < max_ecu_address:
                address, announcement = DoIPClient.await_vehicle_announcement(ipv6=True)
                logical_address = announcement.logical_address
                ip, port, _, _ = address
                send_address = min_ecu_address
                while send_address <= max_ecu_address:
                    self.model.scan_tester_logical_address(ip, logical_address, send_address,
                                                           textbox=self.view.tester.textbox)

                    send_address += 1
            else:
                self.view.diagnostic_frame.show_info_message("Min max error",
                                                             "Minimal address has to be lower then maximal address")

    def scan_did(self, min_did, max_did):
        min_did, max_did = check_hex_numbers(min_did, max_did, view=self.view)
        if min_did is not None and max_did is not None:
            if min_did < max_did:
                if self.model.doip_client is not None:
                    for did_id in range(min_did,max_did+1):
                        self.model.scan_did(did_id, textbox=self.view.discovery.textbox)
                else:
                    self.view.show_info_message("Connection error", "First you need to run tester scan")
            else:
                self.view.show_info_message("Min max error", "Minimal address has to be lower then "
                                                             "maximal address")

    def scan_dtc(self):
        if self.model.doip_client is not None:
            self.model.scan_dtc(textbox=self.view.dtc.textbox)
        else:
            self.view.show_info_message("Connection error", "First you need to run tester scan")

    def generate_pdf(self):
        file1 = open("ECU diagnostic.txt", "w")
        sub_title = 'The ecu parameters'
        file1.write(sub_title)
        text_lines = self.view.ip_model.get_pdf_lines()
        file1.writelines(text_lines)
        text_lines = self.model.dtc_buffer
        file1.writelines(text_lines)
        text_lines = self.model.did_buffer
        file1.writelines(text_lines)
        file1.close()
