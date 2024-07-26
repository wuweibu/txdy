from netmiko import ConnectHandler
import pandas as pd

class Network():
    def __init__(self, ip, username, password, device_type="huawei_vrpv8"):
        device_info = {
            "device_type": device_type,
            "ip" : ip, 
            "port" : 22, 
            "username" : username,
            "password" : password,
        }
        self.ssh = self.conn(device_info)
        self.cpu_data = None
    
    ## Task1: 完善conn函数     连接设备
    def conn(self, device_info):
        return ConnectHandler(**device_info)

    ## Task2: 获取设备CPU信息  并断开连接
    def get_cpu(self):
        self.cpu_data = self.ssh.send_command('display interface',read_timeout=50)
        print(self.cpu_data)
        print(len(self.cpu_data))
        with open('666.txt','w') as f:
            f.write(self.cpu_data)
        self.ssh.disconnect()

    ## Task3: 数据处理找到CPU使用率的几个指标（5秒，1分钟，5分钟）  
    def proc_cpu(self):
        #cpu_line = self.cpu_data.split('CPU utilization for ')[1].split('\n')[0]    #分割数据
        interface = self.cpu_data.split('Output bandwidth utilization :') #通过%分割 取后两位  去除‘ ’      列表表达式
        b=interface[1:]
        print(b)
        for a in b:
            jk=a.split(' current state :')[0]
            print(jk)
        #zt = [one.split('current state :')[0].split('\n')[0] for one in self.cpu_data.split('Last 300 seconds input rate') if one != '']
        #interface = [one.split('current state :')[0] for one in self.cpu_data.split('Last 300 seconds input rate') if one != '']
        #b=interface.split('current state :')[0]
        


## Task4: 调整登录信息，实例化并运行代码
net = Network('172.20.1.254', 'huawei', 'huawei@123')
net.get_cpu()
net.proc_cpu()

# 创建一个excel的行和列
#print(date5)
#date1=date5[0]
#date2=date5[1]
#date3=date5[2]
#print(date1)
#data4 = {'五秒': [date1], '一分钟': [date2],'五分钟':[date3]}
#df = pd.DataFrame(data4)

# 将DataFrame写入Excel文件
#df.to_excel('example_pandas.xlsx', index=False)