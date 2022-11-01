def sol(arr):
    res = []
    arr = sorted(arr)
    for i in range (len(arr)-1):
        if arr[i] + 1 != arr[i+1]:
            res.append(arr[i] + 1)
            if i < len(arr)-1 and arr[i]+2 != arr[i+1]:
                res.append(arr[i] + 2)
    return res
    
    
    
    
    
    
    
    
arr1 = [1,2,8,5,4,3,9,10] #[6,7]
arr2 = [1,2,8,5,3,9,10,6] #[4,7]

print(sol(arr1))
print(sol(arr2))

