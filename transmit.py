import time
import bluetooth
def send_command(bd_addr, command, id_node=5):

    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((bd_addr, 1))  # first port in bluetooth

    command = command + "/%d;" % id_node
    print("Sending command (%s)" % command)
    sock.send(command)
    sock.settimeout(2)
    response = ""
    try:
        while True:
            r = sock.recv(255)
            if not r:
                break

            response = response + r
            if r.find(";") != -1:  # we have reach end of message
                break
    except:
        pass
    print("Response: (%s)" % response)

    sock.close()

def getData(file):
    with open(file, "r") as myfile:
        arr = myfile.readlines()
    length = len(arr)
    string = ",".join(arr)
    string = string.replace('\n', '')
    return string, length
def processdata(file):
    while True:
        try:
            data, length = getData(file)
            #############################
            ##########transmitdata#######
            #############################
            print(data)
            with open(file, "w") as myfile:
                with open(file, "r") as myfile1:
                    filey = myfile1.readlines()
                    del(filey[0:length])
                    myfile.write("".join(filey))

            time.sleep(3)
        except:
            pass
            time.sleep(1)

nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))
print(addr)
send_command(addr, "hello")