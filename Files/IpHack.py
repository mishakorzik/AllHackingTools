from iphack import *
import time

print("01: Ip Address")
print("02: Proxy Checker")
print("03: Proxy Generator")

op = input("Select Option: ")

if op == "1" or op == "01":
    ip_adr = input("While IP: ")
    ip.address(ip_adr)
    time.sleep(60)
if op == "2" or op == "02":
    ip_p = input("While proxy ip: ")
    port_p = input("While proxy port: ")
    check.proxy(ip_p, port_p)
    time.sleep(60)
if op == "3" or op == "03":
    ip.proxy(False)
    time.sleep(60)
