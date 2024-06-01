from netmiko import ConnectHandler

#完成设备基本信息
device_info={
    "device_type":"huawei_vrp",
    "ip":"192.168.1.1",
    "port" : 22,
    "username" : 'huaweiuser',
    "password" : "huawei@123",
}

cmd = "display current-configuration"

#用connecthandler初始化链接     *列表  **字典
net_connect= ConnectHandler(**device_info)

#为任意接口配置IP地址

cmd_list=['system im',
          'interface GE1/0/9',
          'undo shut',
          'undo portswitch',
          'ip add 2.2.2.2 24']
for cmd in cmd_list:
    net_connect.send_command(command_string=cmd,expect_string=']')

#print输出所有接口的信息
cmd='display ip interface brief'
print(net_connect.send_command(cmd))
net_connect.disconnect()

