from doipclient import DoIPClient
from doipclient.connectors import DoIPClientUDSConnector
from udsoncan.Request import *
from udsoncan.Response import *
from udsoncan.client import Client
from udsoncan.services import *
from udsoncan import Dtc


class ECUModelClass:
    def __init__(self, ip_address=None):
        self.ip_address = ip_address
        self.doip_client = None
        self.ecu_logical_address = None
        self.tester_logical_address = None
        self.uds_connection = None
        self.did_buffer = []
        self.dtc_buffer = []

    def end_connection(self):
        self.doip_client.close()

    def byte_separation(self, number):
        return divmod(number, 0x100)

    def scan_did(self, min, max, textbox=None):
        supported_did_codes = []
        self.did_buffer = []
        for did_id in range(min, max):
            my_hex_data = did_id.to_bytes(2, 'big')
            req = Request(services.ReadDataByIdentifier, data=my_hex_data)
            self.uds_connection.send(req.get_payload())
            payload = self.uds_connection.wait_frame(timeout=1)
            response = Response.from_payload(payload)
            if response.code == Response.Code.PositiveResponse:
                supported_did_codes.append(did_id)
                if textbox is not None:
                    textbox.configure(state='normal')
                    text_insert = "Response code " + str(response.code) + " for " + hex(did_id) + " id\n"
                    textbox.insert('end', text_insert)
                    textbox.configure(state='disabled')
                    self.did_buffer.append(text_insert)
            else:
                if textbox is not None:
                    continue
        return supported_did_codes

    def scan_tester_logical_address(self, ip, logical_address, send_address, timeout=2, textbox=None):
        doip_client = DoIPClient(ip, logical_address, client_logical_address=send_address, activation_type=None)
        doip_client.request_activation(0)
        conn = DoIPClientUDSConnector(doip_client)
        try:
            with Client(conn, request_timeout=timeout) as client:
                response = client.change_session(DiagnosticSessionControl.Session.defaultSession)
            if response.positive:
                self.tester_logical_address = send_address
                self.doip_client = doip_client
                self.uds_connection = conn
                self.ecu_logical_address = logical_address
                if textbox is not None:
                    textbox.configure(state='normal')
                    text_insert = "Tester address " + hex(send_address) + " WORKING !!!\n"
                    textbox.insert('end', text_insert)
                    textbox.configure(state='disabled')
                return True

            else:
                if textbox is not None:
                    return False
        except:
            if textbox is not None:
                return False

    def scan_dtc(self, textbox=None):
        self.dtc_buffer = []
        with Client(self.uds_connection, request_timeout=2) as client:
            status = Dtc.Status(True, True, True, True, True, True, True, True)
            response = client.get_dtc_by_status_mask(status)
            save = response.service_data.dtcs
            max = response.service_data.dtc_count
            i = 0
            while i < max:
                textbox.configure(state='normal')
                text_insert = "DTC with id " + hex(save[i].id) + " status " + hex(
                    save[i].status.get_byte_as_int()) + " severity " + hex(save[i].severity.get_byte_as_int()) + "\n"
                textbox.insert('end', text_insert)
                textbox.configure(state='disabled')
                self.dtc_buffer.append(text_insert)
                i += 1
