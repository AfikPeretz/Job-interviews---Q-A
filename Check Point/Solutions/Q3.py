def solution(S):
    dec = 0
    numOper = 0
    for bit in S:
        dec = dec*2
        if bit == '1':
            dec = dec + 1
    while dec > 0:
        if dec % 2 == 0:
            dec //= 2
        else:
            dec -= 1
        numOper += 1
    return numOper


def main():
    arr = [1]
    print(solution(arr))

if __name__ == "__main__":
    main()

