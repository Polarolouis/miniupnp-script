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
print('total bytes : sent', u.totalbytesent(), 'received', u.totalbytereceived())
print('total packets : sent', u.totalpacketsent(), 'received', u.totalpacketreceived())

print(u.addportmapping(12000, 'TCP', u.lanaddr, 12000, 'test port mapping', ''))
input("Hit any key to interrupt port mapping")
print(u.deleteportmapping(12000, 'TCP'))

