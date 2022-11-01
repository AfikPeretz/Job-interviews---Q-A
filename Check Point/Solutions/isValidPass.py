def solution1(a):
    flag = False
    if len(a) < 6:
        return False
    if a.isupper() or a.islower():
        return False
    if not (any(char.isdigit() for char in a)):
        return False
    for char in a:
        if not char.isdigit() and not char.isalpha():
            flag = True
    return flag
        
   


def main():
    s1 = 'anfgld23!' #false
    s2 = 'aN2!' #false
    s3 = 'An123456!' #true
    s4 = 'An123456' #false
    s5 = 'A123b!' #true
    s6 = 'AN123456@' #false
    s7 = 'An!@#$%^' #false
    s8 = 'An!@#$%^6' #true
    
    print(solution1(s1))
    print(solution1(s2))
    print(solution1(s3))
    print(solution1(s4))
    print(solution1(s5))
    print(solution1(s6))
    print(solution1(s7))
    print(solution1(s8))
    

        

if __name__ == "__main__":
    main()