from netmiko import ConnectHandler


#设备的基本信息   992929
device_info = {
    "device_type":"huawei_vrpv8",
    "ip":"172.20.1.254",
    "port":"22",
    "username":"huawei",
    "password":"huawei@123"
}


#初始化链接   字典**
net_connect = ConnectHandler(**device_info)

#为任意接口配置IP地址
#cmd_list=['systerm','interface ge1/0/9','undo shut','undo portswtch','ip add 2.2.2.2 24']
#for cmd in cmd_list:
    #net_connect.send_command(command_string=cmd,expect_string=r']')


#print输出所有接口信息
cmd = 'display interface brief'
data=net_connect.send_command(cmd)
net_connect.disconnect()
print(data)