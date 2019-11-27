import scapy.all as sc
ip=input("IP(only Subnet):\t")
ansl=[]
for j in range(1,11):
    i=sc.ARP(pdst=ip+"."+str(j))
    emptmac=sc.Ether(dst="ff:ff:ff:ff:ff:ff")
    ansl.append(sc.srp(emptmac/i,timeout=1,verbose=False)[0])
def fx():
    print("[+]----------------------------------------------------")
    print ("\tIP Address\t\tM0AC Address")
    for j in ansl:
        for i in j:
            print ("\t"+i[1].psrc+"\t\t"+i[1].hwsrc)

def fx2(ip):
    for j in ansl:
        for i in j:
            if(i[1].psrc==ip):
                return (i[1].hwsrc)


