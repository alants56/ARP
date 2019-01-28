import socket

#主机A的IP地址和UDP端口号
UDP_IP = '192.168.137.3'
UDP_PORT = 10056

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))
print ('Receiving:')
while True:
    data, addr = sock.recvfrom(1024)
    ip=addr[0]
    port = addr[1]
    print(ip + ":" + str(port) +  " msg : " + bytes.decode(data))
