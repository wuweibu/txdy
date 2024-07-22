from netmiko import ConnectHandler
import pandas as pd
import json


def get_login_info(excel_path):
     excel = pd.read_excel(excel_path)
     # dtype,ip,username,password
     data_list = []
     for i in range(excel.shape[0]):                        #循环取出每行数据
         line = excel.loc[i].values.tolist()
         data_list.append(line)
         return data_list

class Net():
    def __init__(self, ip, username, password, device_type=""):
        self.device_info = {
            "device_type": device_type,
            "ip" : ip, 
            "port" : 22, 
            "username" : username,
            "password" : password,
        }
        self.device = self.connect()
    
    # 基本连接功能
    def connect(self):
        return ConnectHandler(**self.device_info)
    
    # 断线重连功能
    def reconnect(self):
        self.device.disconnect()
        self.device = self.connect()

    # 数据输出为json

    def to_json(self,data_dict,file_path):
        with open(file_path,'W') as f:
            # 写文件创建日志
            json.dump(data_dict,fp=f,indent=4)

class VRP_8(Net):
    def _init_(self,dtype,ip,username,password):
        super().__init__(dtype,ip,username,password)

    #获取配置
    #输出字符串形式的设备配置
    def get_config(self):
        cmd='display current-configuration'
        info = self.device.send_command(cmd)
        data_str = ''.join(info.split('#')[1:])
        return data_str