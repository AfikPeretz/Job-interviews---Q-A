#Although it is not written in the question,
#It can be assumed that there is at least one word in s

def lengthOfLastWord(s):
    stack = []
    counter = 0
    for i in range (0, len(s)):
        if s[i] != ' ':
            counter += 1
        else:
            stack.append(counter)
            counter = 0
    stack.append(counter)
    top = len(stack) - 1
    while (stack[top] == 0):
        top -= 1
    return stack[top]