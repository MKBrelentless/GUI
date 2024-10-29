import socket
import math

# TCP server
def tcp_server():
    # create a socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to an address and port
    tcp_socket.bind(("localhost", 8080))
    # listen for incoming connections
    tcp_socket.listen(5)
    print("TCP server is listening")
    
    while True:
        # accept a connection
        conn, addr = tcp_socket.accept()
        print(f"Connected by {addr}")
        # receive the radius
        radius = float(conn.recv(1024).decode())
        # calculate the area
        area = math.pi * radius ** 2
        # send the area back
        conn.sendall(str(area).encode())
        # close the connection
        conn.close()

# Run the server
tcp_server()
