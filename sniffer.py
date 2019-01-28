import socket
import struct
import binascii

#想要截获报文的源ip和目的ip
ip1 = "192.168.137.1"
ip2 = "192.168.137.3"

rawSocket = socket.socket(socket.PF_PACKET,socket.SOCK_RAW,socket.htons(0x0800))
while True :
	pkt = rawSocket.recvfrom(2048)
	ethernetHeader = pkt[0][0:14]   
	eth_hdr = struct.unpack("!6s6s2s",ethernetHeader) 
	binascii.hexlify(eth_hdr[0])
	binascii.hexlify(eth_hdr[1])
	binascii.hexlify(eth_hdr[2])
	ipHeader = pkt[0][14:34]        
	ip_hdr = struct.unpack("!12s4s4s",ipHeader)   
	sIP = socket.inet_ntoa(ip_hdr[1])
	dIP = socket.inet_ntoa(ip_hdr[2])

	#过滤出想要的UDP数据包
	if sIP == ip1 and dIP == ip2 :      
		print ("source IP address: " + sIP)
		print ("destination IP address: " + dIP)
		#去除头部数据，得到UDP数据报文
		data = pkt[0][42:]
		print("msg : " + bytes.decode(data))
		
