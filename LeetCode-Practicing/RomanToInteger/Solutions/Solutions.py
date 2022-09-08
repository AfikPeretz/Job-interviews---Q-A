

def romanToInt(self, s: str) -> int:
        newDict = {"I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000}
        res = 0
        if len(s) == 0: 
            return res
        if len(s) == 1:
            return newDict[s]
        for i in range (0, len(s)-1):
            if newDict[s[i]] < newDict[s[i+1]]:
                res -= newDict[s[i]]
            else:
                res += newDict[s[i]]
        res += newDict[s[len(s)-1]]
        return res