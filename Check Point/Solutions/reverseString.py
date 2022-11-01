

#rows = s.split('\n')
def solution1(s):
    res = ''
    words = s.split(' ')
    for i in range (len(words)-1, -1, -1):
        if i == len(words)-1:
            res += words[i]
        else:
            res += ' '
            res += words[i]
    return res




def solution2(s):
    res = ''
    words = s.split(' ')
    words.reverse()
    for word in words:
        res += word + ' '
    res = res[0:len(res)-1]
    return res
    



def main():
    s = 'my name is afik'
    print(solution1(s))
    print("another solution")
    print(solution2(s))
    
    

        

if __name__ == "__main__":
    main()


