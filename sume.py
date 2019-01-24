import math
def reverse(x):
    list = []
    temp = x
    r = 0
    while(temp != 0):
        list.insert(0,temp%10)
        temp = math.floor(temp/10)


    for i in range(0,len(list)):
        print(list[i])
        c = i

    return temp
if __name__ == "__main__":
    t = 321
    print(reverse(t))
    s = 321/10
    #s = math.ceil(s)
    s = math.floor(s)
    print(s)