

def solution1(s):
    mostinchar = ''
    mostinnum = 0
    for char in s:
        tmp = s.count(char)
        if tmp > mostinnum:
            mostinnum = tmp
            mostinchar = char
    return mostinchar
    
    
        
   


def main():
    s1 = '' #''
    s2 = 'llllldddddrrrrrzzzzz' #l
    s3 = 'wertyuiow' #w
    s4 = '@#$%^&*()_$$' #$
    s5 = 'hey-baby' #y
    s6 = 'afiktheking' #i
    
    
    
    print(solution1(s1))
    print(solution1(s2))
    print(solution1(s3))
    print(solution1(s4))
    print(solution1(s5))
    print(solution1(s6))
    

        

if __name__ == "__main__":
    main()