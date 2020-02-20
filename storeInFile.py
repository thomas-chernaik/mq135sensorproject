import time
import getReadings
getReadings.init()
num = 0
def getData():
    global num
    num += 1
    return str(num)
def store(file, freq):
    while True:
        with open(file, "a") as myfile:
            var = getReadings.read() + "\n"
            myfile.write(var)
            time.sleep(1/freq)

store("hello.txt", 1)