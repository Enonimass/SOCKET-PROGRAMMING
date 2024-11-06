import socket
import sys



# make a packet and pass two parameters(AF_INET, SOCK_STREAM)
try:                                                                       #  AF_INET = refers to the address-family ipv4
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                   # SOCK_STREAM = means connection-oriented TCP protocol.
    print("Socket successfully created")
except socket.gaierror:
    # means unable to resolve the host
    print("socket creation failed with error %s" % (err))

# default port for socket
port = 80

try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:

    #this mean could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

# Connecting tot the server
s.connect((host_ip, port))

print("The socket has successfully connected to google")
