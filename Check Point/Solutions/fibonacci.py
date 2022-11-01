def solution1(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return solution1(n-1) + solution1(n-2)
    
        
   


def main():
    n = 10
    print(solution1(n))
    

        

if __name__ == "__main__":
    main()