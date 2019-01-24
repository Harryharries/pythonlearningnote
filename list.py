import sys

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

print(sys.version)
print(sys.version_info)


