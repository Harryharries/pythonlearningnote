import sys
import random

class Process:
    def __init__(self,name,id,priority,length,odds):
        self.name = name
        self.priority = int(priority)
        self.length = int(length)
        self.id = int(id)
        self.odds = int(odds)

if __name__ == "__main__":
    response = 1
    timeSlice = 5
    type = [0,1,2,3]
    priority = [0,1,2]
    globalTime = 0
    testTIME = 0

    statP0 = 0
    statP1 = 0
    statP2 = 0
    statT0 = 0
    statT1 = 0
    statT2 = 0
    statT3 = 0

    P0 = 0
    P1 = 0
    P2 = 0
    T0 = 0
    T1 = 0
    T2 = 0
    T3 = 0

    FP0 = 0
    FP1 = 0
    FP2 = 0
    FT0 = 0
    FT1 = 0
    FT2 = 0
    FT3 = 0
    # response = sys.argv[1] #input
    # print(response)

    list = []

    with open("read.txt","r") as f:
        for line in f:
            line = line.strip()

            a = line.split(" ")
            process = Process(a[0],a[1],a[2],a[3],a[4])
            list.append(process)
            testTIME += process.length
            if(process.id == 0):
                T0 += 1
                statT0 += 1
            if (process.id == 1):
                T1 += 1
                statT1 += 1
            if (process.id == 2):
                T2 += 1
                statT2 += 1
            if (process.id == 3):
                T3 += 1
                statT3 += 1

            if (process.priority == 0):
                P0 += 1
                statP0 += 1
            if (process.priority == 1):
                P1 += 1
                statP1 += 1
            if (process.priority == 2):
                P2 += 1
                statP2 += 1

    if(response == 1):
        while(len(list) != 0):
            newItem = list.pop(0)

            if(random.randint(1,100) <= newItem.odds):
                ioTime = random.randint(0,5)

                #IO interrept
                if (newItem.length > ioTime):
                    newlength = newItem.length - ioTime
                    newItem.length = newlength
                    list.append(newItem)
                    globalTime += ioTime
                else:
                    globalTime += newItem.length
                    if (newItem.id == 0):
                        FT0 += globalTime
                    if (newItem.id == 1):
                        FT1 += globalTime
                    if (newItem.id == 2):
                        FT2 += globalTime
                    if (newItem.id == 3):
                        FT3 += globalTime
                    if (newItem.priority == 0):
                        FP0 += globalTime
                    if (newItem.priority == 1):
                        FP1 += globalTime
                    if (newItem.priority == 2):
                        FP2 += globalTime

            else:
                if(newItem.length > timeSlice):
                    newlength = newItem.length - timeSlice
                    newItem.length = newlength
                    list.append(newItem)
                    globalTime += timeSlice
                else:
                    globalTime += newItem.length
                    if (newItem.id == 0):
                        FT0 += globalTime
                    if (newItem.id == 1):
                        FT1 += globalTime
                    if (newItem.id == 2):
                        FT2 += globalTime
                    if (newItem.id == 3):
                        FT3 += globalTime
                    if (newItem.priority == 0):
                        FP0 += globalTime
                    if (newItem.priority == 1):
                        FP1 += globalTime
                    if (newItem.priority == 2):
                        FP2 += globalTime


    print("globalTime is:" + str(globalTime))
    print("T:" + str(testTIME))
    print("FT0:" + str(FT3))
    print("SATAT0:" + str(statT3))

    print("There average of pri0 is: " + str(int(FP0/statP0)))
    print("There average of pri1 is: " + str(int(FP1 / statP1)))
    print("There average of pri2 is: " + str(int(FP2 / statP2)))
    print()
    print("There average of type0 is: " + str(int(FT0/statT0)))
    print("There average of type1 is: " + str(int(FT1 / statT1)))
    print("There average of type2 is: " + str(int(FT2 / statT2)))
    print("There average of type3 is: " + str(int(FT3 / statT3)))
