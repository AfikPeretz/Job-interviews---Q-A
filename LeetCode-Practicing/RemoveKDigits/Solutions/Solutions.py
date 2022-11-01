# O(n) complexity, If you didn't pass the question don't be upset, even though the question is listed at the "medium" level,
# it is more difficult than many questions at the "hard" level that I have solved.
def removeKdigits(num, k):
    if len(num) <= k:
        return "0"
    stack = []
    for c in num:
        while k>0 and stack and stack[-1]>c:
            stack.pop()
            k -=1
        stack.append(c)
    stack = stack [: len(stack) - k]
    res = "".join(stack)
    return str(int(res))
