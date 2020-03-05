import time
import datetime
#import getReadings
#getReadings.init()
num = 0
location = input("please enter the location of the device")#need to find a better way of getting the location
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
            #var = getReadings.read() + "," + datetime.datetime.now() + "\n"
            #print(str(datetime.datetime.now()).split(":")[0]) this gives the date and hour
            var = getData() + "," + location + "," + str(datetime.datetime.now()).split(":")[0] + "\n"
            myfile.write(var)
            time.sleep(1/freq)

store("hello.txt", 1)