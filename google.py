def solution(total_money, total_damage, costs, damages):

    c = costs
    d = damages


    for i in range(len(c)):
        tm = total_money#5
        hp = total_damage#3
        if(c[i] >= tm):
            pass
        else:
            newhp = hp - d[i]
            newtm = tm - c[i]
            if(newhp <= 0):
              return True
            else:
                for j in range(i+1, len(c)):
                    if (c[j] >= newtm):
                        pass
                    else:
                        newhp = hp - d[i]
                        if (newhp <= 0):
                            return True
    return False


# write your code in Python 3.6

a = 5
b= 33
c = [4,5,1]
d = [1,2,3]

print(solution(a,b,c,d))