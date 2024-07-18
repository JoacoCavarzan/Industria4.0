from pymodbus.client import ModbusTcpClient
import time

PLC = ModbusTcpClient("127.0.0.1")

PLC.connect()

while True:
    registro = PLC.read_holding_registers(0,1,1)

    print(registro.registers[0])
    time.sleep(0.1)