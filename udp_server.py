import socket
import math

def udp_server():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("localhost", 9090))
    
    print("UDP server is listening")

    while True:
        data, addr = udp_socket.recvfrom(1024)
        print(f"Received data: {data} from {addr}")
        try:
            radius = float(data.decode())
            area = math.pi * radius ** 2
            print(f"Calculated area: {area}")
            udp_socket.sendto(str(area).encode(), addr)
        except ValueError:
            print(f"Invalid data received: {data}")
            udp_socket.sendto(b"Invalid radius", addr)

udp_server()
