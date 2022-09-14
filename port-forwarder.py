#!/usr/bin/python3
import miniupnpc
import sys

u = miniupnpc.UPnP(None, None, 200, 0)
u.lanaddr
u.discover()

try:
    u.selectigd()
except Exception as e:
    print("Exception : ", e)
    sys.exit(1)

print('local ip address :', u.lanaddr)
print('external ip address :', u.externalipaddress())
print( u.statusinfo(), u.connectiontype())



