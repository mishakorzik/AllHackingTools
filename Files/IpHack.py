from iphack import *

print("01: Ip Address")
print("02: Proxy Checker")
print("03: Proxy Generator")

op = input("Select Option: ")

if op == "1" or op == "01":
    ip = input("While ip address: ")
    ip.address(str(ip))
if op == "2" or op == "02":
    ip_p = input("While proxy ip: ")
    port_p = input("While proxy port: ")
    check.proxy(ip_p, port_p)
if op == "3" or op == "03":
    ip.proxy(False)
