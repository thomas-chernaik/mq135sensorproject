import time
import transmitbyinternet

def getData(file):
    with open(file, "r") as myfile:
        arr = myfile.readlines()#stores the lines of the file in an array
    length = len(arr)#stores the length
    string = ";".join(arr)#changes the array to a string joined by ; characters
    string = string.replace('\n', '')#gets rid of newline characters
    return string, length

def processdata(file):
    while True:
        try:
            data, length = getData(file)
            #now send
            url = ("https://smello-vision.herokuapp.com/readings")# the ip address and the port of the server
            if(data != ""):#if there is data to send
                transmitbyinternet.sendData(bytes(data, "utf-8"), url)#sends the data via websocket

            # it will error before here if the data doesn't send successfully
            with open(file, "w") as myfile:
                with open(file, "r") as myfile1:
                    filey = myfile1.readlines()
                    del(filey[0:length])
                    myfile.write("".join(filey))

                    #clears the file so data isn't send twice

            time.sleep(10)
        except Exception as e:
            print(e)
            time.sleep(60)
"""
nearby_devices = bluetooth.discover_devices(lookup_names=True)
print("Found {} devices.".format(len(nearby_devices)))

for addr, name in nearby_devices:
    print("  {} - {}".format(addr, name))
print(addr)
send_command(addr, "hello")
"""
processdata("hello.txt")
