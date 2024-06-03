from netmiko import ConnectHandler

class Network():
    def __init__(self, ip, username, password, device_type="huawei_vrpv8"):
        device_info = {
            "device_type": device_type,
            "ip" : ip, 
            "port" : 22, 
            "username" : username,
            "password" : password
        }
        self.device = self.conn(device_info)
        self.cpu_data = None
    
    ## Task1: 完善conn函数
    def conn(self, device_info):
        return ConnectHandler(**device_info)


    ## Task2: 获取设备CPU信息
    def get_cpu(self):
        self.cpu_data = self.device.send_command('dis cpu')
        return self.cpu_data


    ## Task3: 数据处理找到CPU使用率的几个指标（5秒，1分钟，5分钟）
    def proc_cpu(self):
        cpu_line = self.cpu_data.split('CPU utilization for ')[1].split('.')[0]
        data_list = [one[-1:] for one in cpu_line.split('%') if one != '']
        print(data_list)


## Task4: 调整登录信息，实例化并运行代码
net = Network('172.20.1.254', 'huawei', 'huawei@123')
net.get_cpu()
net.proc_cpu()