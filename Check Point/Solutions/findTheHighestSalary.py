
#rows = s.split('\n')
def solution1(s):
    res = 0
    tmp = ''
    for i in range (len(s)):
        if s[i].isdigit():
            tmp += s[i]
        else:
            if tmp:
                tmp = int(tmp)
                if res < tmp:
                    res = tmp
                tmp = ''
    tmp = int(tmp)
    if res < tmp:
        res = tmp
    return res



def solution2(s):
    maxsalary = 0
    rows = s.split('\n')
    for row in rows:
        tmp = row.split(',')
        if len(tmp) == 3:
            if int(tmp[2]) > maxsalary:
                maxsalary = int(tmp[2])
    return maxsalary
    



def main():
    s = 'name,salary\n1,itay,22000\n2,rami,23000\n3,afik,30000'
    print(solution1(s))
    
    

        

if __name__ == "__main__":
    main()


