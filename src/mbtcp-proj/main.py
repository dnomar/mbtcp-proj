from pyModbusTCP.client import ModbusClient

class ModbusTCPReader:
    def __init__(self, host, port):
        self.mbtcp = ModbusClient()
        self.host = host
        self.port = port

    def mbtcp_read(self):
        if not self.mbtcp.host(self.host):
            print("Error de Host")
        if not self.mbtcp.port(self.port):
            print("Error de Puerto")
        return self.mbtcp

    def mbtcp_close(self, arg):
        arg.close()


if __name__ == "__main__":
    c = ModbusTCPReader("localhost", 502)
    print(c.mbtcp_read())
    c.mbtcp_close(c.mbtcp_read())
