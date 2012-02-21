

result = []

def isPal(num):
    strNum = str(num)
    middle = int(len(strNum)/2)
    first = strNum[0:middle]
    if len(strNum)%2 == 0:
        second = strNum[middle:]
    else:
        second = strNum[middle+1:]
    if first == second[::-1]:
        return True
    else:
        return False

def isBinPal(strBinNum):
    middle = int(len(strBinNum)/2)
    first = strBinNum[0:middle]
    if len(strBinNum)%2 == 0:
        second = strBinNum[middle:]
    else:
        second = strBinNum[middle+1:]
    if first == second[::-1]:
        return True
    else:
        return False
        

def main():
    for x in range(1,1000001):
        if isPal(x) and isBinPal(bin(x)[2:]):
            print(x)
            result.append(x)
    summ = 0
    for x in result:
        summ = summ + x
    print(summ)

def testIsPal():
    if not isPal(3):
        print("Alarm", 3)
    if not isPal(585):
        print("Alarm",585)

    if not isBinPal('11'):
        print("Alarm",'11')

    if not isBinPal('10000001'):
        print("Alarm",'10000001')        
