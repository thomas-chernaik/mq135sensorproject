import socket, time
"""
ipport is a tuple of IP address, port
"""
def sendData(data, ipport):
    # Create a socket object
    s = socket.socket()
    # connect to the server
    s.connect(ipport)

    # receive data from the server
    s.send(data)
    # close the connection
    s.close()