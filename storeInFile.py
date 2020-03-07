import time
import datetime
import random
#import getReadings
#getReadings.init()
num = 0.0
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
    num = random.random()
    return str(num)
def store(file, freq):
    i=0
    while True:
        with open(file, "a") as myfile:
            with open("location.txt", "r") as myfile1:
                location = myfile1.read().replace('\n','')
            #var = getReadings.read() + "," + datetime.datetime.now() + "\n"
            #print(str(datetime.datetime.now()).split(":")[0]) this gives the date and hour
            now = datetime.datetime.now()
            strnow = now.strftime("%Y-%m-%d-%H-%M-%S")
            #print(strnow)
            #var = getData() + "," + location + ",50.0,-0.1,"  + strnow + "\n"
            gps = "50.0,-0.1"
            var = "%s,%s,%s,%s\n" %(strnow, location, gps, getData())#change to getreadings
            print(bytes(var, 'utf-8'))
            myfile.write(var)
            time.sleep(1/freq)
            i+=1
            if i==1000:
               break

store("hello.txt", 1)
