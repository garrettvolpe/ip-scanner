from ping3 import ping
import socket

network= "192.168.50."
ip_start_range = 1
ip_end_range = 254
list_of_ips = []
online_ips = []
print(ip_end_range)

while ip_start_range != ip_end_range:
    print(ip_start_range)
    list_of_ips.append(network + str(ip_start_range))
    ip_start_range += 1

for a in list_of_ips:
    print(a)
    response = ping (a)
    if response != False:
        print (a)
        online_ips.append(a)

print(online_ips)

