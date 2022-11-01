def solution(S, C):
    tbl = []
    rows = S.split("\n")  
    for row in rows:
        col = row.split(",")
        tbl.append(col)
    for i in range(len(tbl[0])):
        col_name = tbl[0][i]
        if col_name == C:
            res = float("-Inf")
            for y in range(1, len(tbl)):
                res = max(res, int(tbl[y][i])) 
            return res

def main():
    solution(S, C)

if __name__ == "__main__":
    main()
