# O(n)
def isPalindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    if len(s) == 1 or len(s) == 0:
        return True
    firstHalf = ''
    secondHalf = ''
    if (len(s)%2 == 0):
        firstHalf = s[0 : len(s)//2]  
        secondHalf = s[(len(s)//2) : len(s)]   
    else:
        firstHalf = s[0 : len(s)//2]
        secondHalf = s[len(s)//2 + 1 : len(s)]
    for i in range (0, len(s)//2):
        if firstHalf[i] != secondHalf[len(s)//2 - 1 - i]:
            return False
    return True