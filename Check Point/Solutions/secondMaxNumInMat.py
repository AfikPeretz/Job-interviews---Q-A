

def solution1(a):
    res = []
    if len(a) == 0:
        return None
    for i in range(len(a)):
        for j in range (len(a[0])):
            res.append(a[i][j])
    res = sorted(res)     
    return res[-2]

    



def main():
    arr1 = [[3,8,111,22],[-1,0,43,4500],[-700,-346,700,346],[0,0,0,0]]
    arr2 = [[3,8,111],[-1,112,43],[-700,-346,700],[0,0,0]]
    arr3 = [[3,8,111],[-1,0,43],[-700,-346,700]]
    
    print(solution1(arr1))
    print(solution1(arr2))
    print(solution1(arr3))
    

        

if __name__ == "__main__":
    main()


