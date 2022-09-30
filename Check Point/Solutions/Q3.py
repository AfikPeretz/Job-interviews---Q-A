def ans(a):
    minstrokes = 0
    for i in range (1,max(a)+1):
        tmp = minstrokes
        for j in range (len(a)-1):
            if a[j] == i:
                if a[j-1]:
                    if a[j-1] != i:
                        minstrokes += 1
        if tmp == minstrokes:
            minstrokes += 1
    return minstrokes
