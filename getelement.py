import scapy.all as scapy

def scanner(ip):
    request = scapy.ARP(pdst = ip)

    broadcast = scapy.Ether()
    broadcast.dst = "ff:ff:ff:ff:ff:ff"
    #broadcast.show()

    request_broadcast = broadcast/request
    #request_broadcast.show()

    resp1 = scapy.srp(request_broadcast,timeout = 1)[0]

    for el in resp1:
        print(el[1].psrc)
        print(el[1].hwsrc)
        print("---------------------------------------------------------------------")

    #print(broadcast.summary())
   # scapy.ls(scapy.Ether())
scanner("192.168.178.1/24")
