import socket, time, requests
"""
ipport is a tuple of IP address, port
"""
def sendDataSocket(data, ipport):
    # Create a socket object
    s = socket.socket()
    # connect to the server
    s.connect(ipport)

    # receive data from the server
    s.send(data)
    # close the connection
    s.close()


def sendData(data, address):
    r = requests.post(address, files={'file': data})