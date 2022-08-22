def solution(s):
    flag = True
    stack = []
    my_set = {'(', '{', '['}
    for char in s:
        if char in my_set:
            stack.append(char)
        if char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                flag = False
        if char == '}':
            if len(stack) == 0 or stack.pop() != '{':
                flag = False
        if char == ']':
            if len(stack) == 0 or stack.pop() != '[':
                flag = False
    if len(stack) != 0:
        flag = False
    return flag


def main():
    s = "(){[]}{[}]"
    print(solution(s))

if __name__ == "__main__":
    main()

