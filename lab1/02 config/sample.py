from netmiko import ConnectHandler

device_info = {
    "device_type":"huawei_vrpv8",
    "ip":"172.20.1.254",
    "port":"22",
    "username":"huawei",
    "password":"huawei@123"
}

cmd = "display current-configuration"

#初始化链接   字典**
net_connect = ConnectHandler(**device_info)

#发送命令获取配置
result = net_connect.send_command(cmd)
print(result)

#处理数据并保存到本地
data = 'aaa' + result.split('aaa')[1]    #字符串拼接
with open('huawei_config.cfg','w')as f:
    f.write(data)
with open ('huawei_config.cfg') as f:
    new_data=f.read()
print(new_data)