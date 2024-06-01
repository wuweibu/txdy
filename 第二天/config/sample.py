from netmiko import ConnectHandler

#完成设备基本信息
device_info={
    "device_type":"huawei_vrpv8",
    "ip":"192.168.1.1",
    "port" : 22,
    "username" : 'huaweiuser',
    "password" : "huawei@123",
}

cmd = "display current-configuration"

#用connecthandler初始化链接     *列表  **字典
net_connect= ConnectHandler(**device_info)

#发送命令获取配置
result = net_connect.send_command(cmd)
print(result)
net_connect.disconnect()

#处理数据并保存在本地
data ='aaa'+ result.split('aaa')[1]
with open('huawei_config.cfg','w')as f:
    f.write(data)
with open('huawei_config.cfg')as f:
    new_data=f.read()                                  #读取成一个大字符串  readlines读成一个列表 readline读取一行退出
print(new_data)