def getNum(var):
    delta = 1
    for x in range(1,round(var/2)):
        if (var%x) == 0:
            delta = delta+1
    return delta
