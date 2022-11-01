

def solution(intervals):
    out = []
    intervals = sorted(intervals)
    for i in intervals:
        if out and i[0] <= out[-1][1]:
            out[-1][1] = max(out[-1][1], i[1])
        else:
            out += [i]
    return out

    
    



def main():
    arr = [[1,3],[2,6],[8,10],[15,18],[5,7]]
    print(solution(arr)) #[[1, 7], [8, 10], [15, 18]]
    

        

if __name__ == "__main__":
    main()


