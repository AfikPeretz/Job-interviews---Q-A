def solution1(a):
    res = []
    a = sorted(a)
    for i in range (len(a)):
        if len(res) == 0 and i != a[i]-1:
            res.append(i+1)
            a.append(i+1)
            break
    a = sorted(a)
    for i in range (len(a)):
        if i != a[i]-1:
            res.append(i+1)
            break
    if len(res) == 0:
        res.append(a[len(a)-1] + 1)
        res.append(a[len(a)-1] + 2)
    if len(res) == 1:
        res.append(a[len(a)-1] + 1)
    return res




def main():
    arr1 = [1,2,8,5,4,3,9,10] #[6,7]
    arr2 = [1,2,8,5,4,3,6,7] #[9,10]
    arr3 = [6,7,8,5,4,3,9,10] #[1,2]
    arr4 = [2,8,5,4,3,9,6,7] #[1,10]
    arr5 = [1,2,8,5,3,9,10,6] #[4,7]
    
    print(solution1(arr1))
    print(solution1(arr2))
    print(solution1(arr3))
    print(solution1(arr4))
    print(solution1(arr5))
    

        

if __name__ == "__main__":
    main()