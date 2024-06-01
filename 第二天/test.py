qaz=['1.1.1.1','2.2.2.2','3.3.3.3']
wsx={'ip':'1.1.1.1','name':'wwb'}

def wjwj(ip1,ip2,ip3):
    print(ip1)
    print(ip2)
    print(ip3)

wjwj(*qaz)

def wewe(ip,name):
    print(ip)
    print(name)

wewe(**wsx)