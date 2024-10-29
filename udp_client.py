import socket

def udp_client(radius):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(f"Sending radius: {radius}")
    udp_socket.sendto(str(radius).encode(), ("localhost", 9090))
    
    try:
        area, _ = udp_socket.recvfrom(1024)
        print(f"UDP: The area of the circle is {area.decode()}")
    except socket.timeout:
        print("No response from the server, timeout!")
    
    udp_socket.close()

radius = 5
udp_client(radius)
