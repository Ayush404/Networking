import socket
import os
import struct

def analyze_ether_header(data):
    eth_hdr = struct.unpack("!6s6s2H" , data[:16]) #IPv4 = 0x0800
    dest_mac = eth_hdr[0] #Destination Address
    src_mac  = eth_hdr[1] #Source mac
    proto    = eth_hdr[2] #Next Protocol

    print (dest_mac)
    print (src_mac)
    print (hex(proto))

    data = data[16:]
    return

def main():
    sniffer_socket=socket.socket(socket.PF_PACKET , socket.SOCK_RAW , socket.htons(0x0003))
    #sniffer_socket.bind(()) <===== DONT DO THIS bcz its a raw socket and not going to any specific port.Its going to only listen to that port!
    recv_data = sniffer_socket.recv(2048)
    print (recv_data)

    data = analyze_ether_header(recv_data)

while True:
    main()
