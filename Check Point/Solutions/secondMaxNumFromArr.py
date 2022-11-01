
def solution1(a):
    a = sorted(a)
    return a[-2]
    
    
    
def solution2(a):
    maxfroma = max(a)
    a.remove(maxfroma)
    return max(a)


    



def main():
    arr1 = [2,7,3,41,1,55,32,1000,-7, 0, 430,500]
    arr2 = [2,7,3,41,1,55,32,1000,-7, 0, 430,500, 1000]
    print("solution1")
    print(solution1(arr1))
    print(solution1(arr2))
    print("solution2")
    print(solution2(arr1))
    print(solution2(arr2))

        

if __name__ == "__main__":
    main()


