import socket

#将MESSAGE通过UDP发送给主机A

#主机A的IP地址和UDP端口号
UDP_IP = '192.168.137.3'
UDP_PORT = 10056
MESSAGE = b'Hello win7!'

for i in range(3) :
    print ('UDP destination IP：', UDP_IP)
    print ('UDP port：', UDP_PORT)
    print ('msg：', bytes.decode(MESSAGE))
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))