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

#数据处理找到cpu使用率的几个指标（5秒，1分钟，5分钟）
result = net_connect.send_command('dis cpu')
cpu_line=result.split('cpu utilization for')[1].split('.')[0]
data_list = [one[-1:] for one in cpu_line.split('%') if one != '']   #循环cpu_line分割%，最后一个字符，不等于空
print(data_list)


