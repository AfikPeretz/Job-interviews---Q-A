def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        newS = ""
        for r in range(numRows):
            jump = 2*(numRows-1)
            for i in range(r, len(s), jump):
                newS += s[i]
                if(r > 0 and r < numRows - 1 and i + jump -2 * r < len(s)):
                    newS += s[i + jump -2 * r]
        return newS