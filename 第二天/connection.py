import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from netmiko import ConnectHandler

usermail = "A973962717@tom.com"
password = "wwb991214"
alert_mail = "973962717@qq.com"
smtpserver = "smtp.tom.com"
smtpport = 25

class Net():
    def __init__(self, ip, username, password, device_type="huawei_vrpv8"):
        device_info = {
            "device_type": device_type,
            "ip" : ip, 
            "port" : 22, 
            "username" : username,
            "password" : password
        }
        self.device = self.connect(device_info)
        self.cpu_data = None

    def connect(self,device_info):
        return ConnectHandler(**device_info)
    
    
    def to_json(self,data_dict,file_path):
        with open(file_path,'w')as f:
            json.dump(data_dict,fp=f,indent=4)

    def send_mail(self,subject,boby):
        message = MIMEText(boby,'html','utf-8')
        message['Subject'] = Header(subject,'utf-8')
        message['From']= usermail
        message['To'] = alert_mail
        sender = smtplib.SMTP(smtpserver,smtpport)
        sender.login(usermail,password)
        sender.sendmail(usermail,alert_mail,message)
        sender.quit()


net = Net('172.20.1.254','huawei','huawei@123')

cmd = 'display cur'
info = net.device.send_command(cmd)
print(info)

    