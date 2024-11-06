import socket

#create a socket object
s = socket.socket()
print("socket successfully created")

'''
reserve a port in your computer
case it is 12345 but it can be anything  '''
port = 12345

'''
Next bind to the port
no ip in the ip field is typed
instead an empty string is inputted
this makes server listen to requests coming form other computers on the network
'''
s.bind(('', port))
print("socket binded to %s" %(port))

# put socket on listening mode
s.listen(5)

'''create a forever loop until its interrupted or
an error occurs'''
while True:

    # establish a connection with the client
    c, addr = s.accept()
    print("Got connection from", addr)

    #Send a thank-you message to the client. encoding to send byte type.
    c.send("Thank you for connecting".encode())

    #close the connection with the client
    s.close()

    #break once the connection is closed
    break