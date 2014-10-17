def turnIntoList(num1,num2,num3):
    list1 = [num1,num2,num3]
    return list1
    
print turnIntoList(5,10,15)


def getFirstInList(list1):
    print list1[0]
    
getFirstInList([5,1,85,62,64,74])


def getLastInList(list2):
    print list2[len(list2) - 1]
    
getLastInList([99,54,21,8,4])


def swapFirstAndLast(list3):
    firstPos = list3[0]
    lastPos = list3[len(list3) - 1]
    list3[0] = lastPos
    list3[len(list3) - 1] = firstPos
    return list3

print swapFirstAndLast([54,21,84,98])