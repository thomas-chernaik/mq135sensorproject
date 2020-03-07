import time
import datetime
import bluetoothgetLocation
#import getReadings
#getReadings.init()
num = 0
#location = input("please enter the location of the device")#need to find a better way of getting the location

while True:
    with open("location.txt", "r") as myfile:
        if myfile.read() != "":
            
            break



def getData():
    ###################################
    #this function is just for testing#
    ###################################
    global num
    num += 1
    return str(num)
def store(file, freq):
    while True:
        with open(file, "a") as myfile:
            with open("location.txt", "r") as myfile:
                location = myfile.read()
            #var = getReadings.read() + "," + datetime.datetime.now() + "\n"
            #print(str(datetime.datetime.now()).split(":")[0]) this gives the date and hour
            now = datetime.datetime.now()
            strnow = now.strftime("%Y-%m-%d-%H-%M-%s")
            print(strnow)
            var = getData() + "," + location + ",50.0,-0.1,"  + strnow + "\n"
            myfile.write(var)
            time.sleep(1/freq)

store("hello.txt", 1)