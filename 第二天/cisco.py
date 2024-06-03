from connection import Net



class IOS_XE_17(Net):
    def __init__(self):
        super().__init__('huawei','172.20.1.254','huawei','Huawei123')

    def get_config(self):
        cmd='dis cu'