from netmiko import ConnectHandler

## Task1: 完成设备基本信息
device_info = {
    "device_type": "huawei_vrpv8",
    "ip" : '172.20.1.254', 
    "port" : 22, 
    "username" : 'huawei',
    "password" : 'huawei@123',
}

cmd = "display current-configuration"

## Task2: 用ConnectHandler初始化链接   ssh连接
net_connect = ConnectHandler(**device_info)

## Task3: 发送命令获取配置
result = net_connect.send_command(cmd)
net_connect.disconnect()       #断开SSH连接

## Task4: 处理配置数据并保存在本地
date = result
data = 'aaa' + result.split('aaa')[1]
with open('huawei_config.cfg', 'w') as f:
    f.write(data)
with open('huawei_config.cfg') as f:
    new_data = f.read()
print(new_data)