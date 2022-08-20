def solution(s):
    flag = True
    stack = []
    char1, char2, char3  = '(', '{', '['
    for char in s:
        if char == char1:
            stack.append(char1)
        if char == char2:
            stack.append(char2)
        if char == char3:
            stack.append(char3)
        if char == ')':
            if len(stack) == 0 or stack.pop() != char1:
                flag = False
        if char == '}':
            if len(stack) == 0 or stack.pop() != char2:
                flag = False
        if char == ']':
            if len(stack) == 0 or stack.pop() != char3:
                flag = False
    if len(stack) != 0:
        flag = False
    return flag


def main():
    s = "(){[]}"
    print(solution(s))

if __name__ == "__main__":
    main()

