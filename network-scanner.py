from scapy.all import *
import socket

arpkt = Ether() / ARP()
arpkt[Ether].dst = "ff:ff:ff:ff:ff:ff"
arpkt[ARP].src = "a0:51:0b:50:35:43"
arpkt[ARP].hwsrc = "a0:51:0b:50:35:43"
arpkt[ARP].pdst = "172.20.10.1/24"
result = srp(arpkt, timeout=10)[0]
clients = []
for sent, received in result:
    clients.append({'ip': received.psrc, 'mac': received.hwsrc})
print("Available devices in the network:")
print("IP" + " " * 18 + "MAC")
for client in clients:
    print("{:16}    {}".format(client['ip'], client['mac']))
print('finished to scan hosts and begin scan for open ports ')
ip_address = []
for ip in clients:
    ip_address.append(ip['ip'])
def is_port_open():
    ports = [80, 445, 139, 3389, 21, 22]

    for ipaddr in ip_address:
      for port in ports:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            conn = s.connect_ex((ipaddr,port))
            # print(ipaddr ,port)
            if conn == 0:
                print(f"on {ipaddr} port {port} is open")
            if conn == 1:
                print(ipaddr ,":" ,port)
            s.close()
        except Exception as e:
            print(e)


is_port_open()

