def solution1(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                tmp = stack.pop()
                if tmp != '(':
                    return False
            else:
                return False
    if stack:
        return False
    return True


def solution2(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
    
    
    
        
   


def main():
    s1 = '(((())))' #true
    s2 = '()()(())()((()))'#true
    s3 = '())' #false
    s4 = '(())(())(()' #false
    s5 = '(' #false
    s6 = ')' #false
    
    print(solution1(s1))
    print(solution1(s2))
    print(solution1(s3))
    print(solution1(s4))
    print(solution1(s5))
    print(solution1(s6))
    
    print('solution2')
    
    print(solution2(s1))
    print(solution2(s2))
    print(solution2(s3))
    print(solution2(s4))
    print(solution2(s5))
    print(solution2(s6))
    

        

if __name__ == "__main__":
    main()