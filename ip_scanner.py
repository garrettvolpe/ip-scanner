from ping3 import ping
import socket

network= "192.168.50."
ip_start_range = 1
ip_end_range = 254
list_of_ips = []
online_ips = []

while ip_start_range != ip_end_range:
    list_of_ips.append(network + str(ip_start_range))
    ip_start_range += 1

for a in list_of_ips:
    response = ping (a)
    if response != None:
        print (a)
        print(response)
        online_ips.append(a)

print(online_ips)

for t in online_ips:
    try:
        hostname = socket.gethostbyaddr(t)
        print(hostname)
    except:
        pass
     # print(hostname[0],hostname[2])
