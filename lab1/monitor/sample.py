from netmiko import ConnectHandler


#设备的基本信息
device_info = {
    "device_type":"huawei_vrpv8",
    "ip":"172.20.1.254",
    "port":"22",
    "username":"huawei",
    "password":"huawei@123"
}

#初始化链接   字典**
net_connect = ConnectHandler(**device_info)


## 获取设备cpu信息



##数据处理找到cpu使用率的几个指标（5秒，1分钟，5分钟）
result = net_connect.send_command('dis cpu')
cpu_line = result.split('CPU utilization for')[1].split('.')[0]
data_list = [one[-1:] for one  in cpu_line.split('%') if one != '']
print(data_list)