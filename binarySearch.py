def binarySearch(thelist,item):
    first = 0
    last = len(thelist) -1
    done = False

    while first < last and not done:
        mid = (first+last)//2

        if thelist[mid] == item:
            done = True
        else:
            if item<thelist[mid]:
                last = mid -1;
            else:
                first= mid+1;
    return done


if __name__ == "__main__":
    list = [0,1,2,3,4,56,77,88]
    print(binarySearch(list,int(77)))