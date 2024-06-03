from connection import Net
from netmiko import ConnectHandler

net = Net('huawei_vrpv8','172.20.1.254','huawei','huawei@123')

cmd = 'display cur'
info = net.device.send_command(cmd)

print(info)