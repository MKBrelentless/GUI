import socket

# TCP client
def tcp_client(radius):
    # create a socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connect to the server
    tcp_socket.connect(("localhost", 8080))
    # send the radius
    tcp_socket.sendall(str(radius).encode())
    # receive the area
    area = tcp_socket.recv(1024).decode()
    print(f"TCP: The area of the circle is {area}")
    # close the socket
    tcp_socket.close()

# Example usage
radius = 5
tcp_client(radius)
