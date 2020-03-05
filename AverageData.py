def average(filename):
    with open(filename, "r") as myfile:
        data = myfile.readlines()
        #stores each line of the file in an array
    del(data[0])#deletes the first line which is the key
    data1 = []
    for i in data:
        #print(i)
        data1.append(i.strip("\n").split(","))#strips all the newline characters and splits into arrays at commas
    dict = {}
    for i in data1:
        dict[i[0]] = [0,0]#initialises the dictionary for putting data into
    for i in data1:
        #print(i)
        dict[i[0]][0] += int(i[1])#the total value
        dict[i[0]][1] += 1#the count
    newData = []
    for i in dict:
        print(i)
        newData.append(i + "," + str(dict[i][0] / dict[i][1]) + "\n")#this calculates the mean
    print(newData)
    newData = ["District,Pollution\n"] + newData#adds the key
    with open(filename, "w") as myfile:
        myfile.writelines(newData)#writes the data to a file

average("data.txt")