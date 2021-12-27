from scapy.all import *
import sys

# Complete this function!
def process_pcap(pcap_fname):
    ip_addresses = {}

    for pkt in PcapReader(pcap_fname):
        if pkt.haslayer(IP) and pkt.haslayer(TCP):
            # SYN packet
            if pkt[TCP].flags == 'S':
                if pkt[IP].src not in ip_addresses:
                    ip_addresses[pkt[IP].src] = {'SYN_sent': 0, 'SYN_ACK_received': 0}
                    ip_addresses[pkt[IP].src]['SYN_sent'] = 1
                else:
                    ip_addresses[pkt[IP].src]['SYN_sent'] += 1
            # SYN+ACK packet
            elif pkt[TCP].flags == 'SA':
                if pkt[IP].dst not in ip_addresses:
                    ip_addresses[pkt[IP].dst] = {'SYN_sent': 0, 'SYN_ACK_received': 0}
                    ip_addresses[pkt[IP].dst]['SYN_ACK_received'] = 1
                else:
                    ip_addresses[pkt[IP].dst]['SYN_ACK_received'] += 1
    
    for ip in ip_addresses:
    	# IP address that sent more than 3 times SYN packets than SYN+ACK packets received
        if ip_addresses[ip]['SYN_sent'] > (ip_addresses[ip]['SYN_ACK_received'] * 3):
            print(ip)

if __name__=='__main__':
    if len(sys.argv) != 2:
        print('Use: python3 detector.py file.pcap')
        sys.exit(-1)
    process_pcap(sys.argv[1])