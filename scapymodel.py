import scapy.all as scapy

def scanner(ip):
    request = scapy.ARP(pdst = ip)
    #request.pdst = ip
    #request.show()
    #print(request.summary())
    # scapy.arping(ip)
   # print(request.summary())
   # scapy.ls(scapy.ARP())

    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    #broadcast.show()

    request_broadcast = broadcast/request
    #request_broadcast.show()

    resp1,resp2 = scapy.srp(request_broadcast,timeout = 1)

    for el in resp1:
        print(el)

    #print(broadcast.summary())
   # scapy.ls(scapy.Ether())

scanner("192.168.178.1/24")