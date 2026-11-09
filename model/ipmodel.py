class IPModelClass:
    def __init__(self, ip_address=None, interface=None, ip_name=None, ecu_bool=False, mac_address=None,
                 ping_response=False,
                 ping_response_time=0, save_name="Default save", vlan_bool=False, vlan_id=0):
        self.ip_address = ip_address
        self.interface = interface
        self.ip_name = ip_name
        self.ecu_bool = ecu_bool
        self.mac_address = mac_address
        self.ping_response = ping_response
        self.ping_response_time = ping_response_time
        self.save_name = save_name
        self.vlan_bool = vlan_bool
        self.vlan_id = vlan_id

    def get_pdf_lines(self):
        lines = ["Ip address is: " + self.ip_address + "\n", "Used interface: " + self.interface + "\n"]
        if self.ip_name is not None:
            lines.append("Name of ip address: " + str(self.ip_name) + "\n")
        if self.mac_address is not None:
            lines.append("Mac_address: " + self.mac_address + "\n")
        if self.ping_response is not False:
            lines.append("Responds to ping: " + str(self.ping_response) + "\n")
            lines.append("Response time for ping is " + str(self.ping_response_time) + "ms" + "\n")
        if self.vlan_bool is not False:
            lines.append("Vlan used: " + str(self.vlan_bool) + "\n")
            lines.append("Vlan id: " + str(self.vlan_id) + "\n")
        return lines
