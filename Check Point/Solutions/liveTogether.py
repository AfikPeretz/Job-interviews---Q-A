

def solution1(logs):
    maxcounter = 0
    res = 0
    for i in range (len(logs)):
        tmp = 0
        for j in range (len(logs)):
            curBorn, othersDie, othersBorn = logs[i][0], logs[j][1], logs[j][0]
            if curBorn >= othersBorn and  curBorn < othersDie:
                tmp += 1
                if tmp > maxcounter:
                    maxcounter = tmp
                    res = logs[i][0]
                elif tmp == maxcounter:
                    res = min(res,logs[i][0])
    return res
        
            

    



def main():
    arr1 = [[1984, 2014],[1998, 2042],[2005, 2044],[2039, 2047]]
    print(solution1(arr1)) #2005
    

        

if __name__ == "__main__":
    main()


