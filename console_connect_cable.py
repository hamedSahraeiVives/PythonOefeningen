from netmiko import connectHandler
connection = connectHandler(device_type = "cisco_ios_serial", serial_setting = {"port" : "COM5", "baudrate": 9600})
print(connection.check_enable_mode())
print(connection.send_command("show version"))

