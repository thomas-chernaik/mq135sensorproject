# first of all import the socket library
import socket
import time
timer = time.time()
# next create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve a port on your computer in our
port = 8000
print(socket.gethostname())
# coming from other computers on the network
s.bind(("", port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")
print(time.time() - timer)
# a forever loop until we interrupt it or
# an error occurs
while True:
    try:
        # Establish connection with client.
        c, addr = s.accept()
        print(c.recv(1000000000000000000000000000).decode("utf-8"))
        print('Got connection from', addr)
        cfile = c.makefile('rw', 0)
        line = cfile.readline().strip()
        cfile.write('HTTP/1.0 200 OK\n\n')
        cfile.write('<html><head><title>Welcome %s!</title></head>' % (str(addr)))
        #with open("index.html", "rb") as myfile:
         #   c.send(myfile.read())
            #c.close()
        """
        datarecvd = c.recv(1000000000000000000000000000).decode("utf-8")
        print("hey")
        data = []
        dataformatted = datarecvd.split(";")
        for i in dataformatted:
            data.append((i).split(","))
            #print(data)
        print(data)
        for i in data:
            with open(str(i[2]), "a+") as myfile:
                myfile.write(i[1] + "," + i[0] + "\n")
            with open(str(i[2]), "r") as myfile:
                data1 = myfile.readlines()
                if(data1[0] != "District,Pollution\n"):
                    with open(i[2], "w") as myfile1:
                        myfile1.writelines(["District,Pollution\n"]+myfile.readlines())
        # Close the connection with the client
        #c.close()
        """
        c.close()
        input()
        print(time.time())
    except:
        pass
