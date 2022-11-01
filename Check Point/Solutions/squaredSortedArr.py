def solution1(arr):
    res = []
    for i in arr:
        res.append(i**2)
    res = sorted(res)
    return res
    
    
    
        
   


def main():
    arr = [-100, -73, -42, -11, -3, 0, 4, 7, 32, 76, 178, 542]
    print(solution1(arr))
    

        

if __name__ == "__main__":
    main()