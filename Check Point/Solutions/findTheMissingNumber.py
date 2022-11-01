def solution1(a):
    a = sorted(a)
    for i in range (len(a)):
        if i != a[i]-1:
            return i+1
    return a[len(a)-1] + 1
    
        
   


def main():
    arr = [1,7,2,8,9,5,4,3,6]
    
    print(solution1(arr))
    

        

if __name__ == "__main__":
    main()