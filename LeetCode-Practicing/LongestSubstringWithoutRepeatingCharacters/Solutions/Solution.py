class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        le = 0
        sol = 0
        for i in range(len(s)):
            while s[i] in my_set:
                my_set.remove(s[le])
                le += 1
            my_set.add(s[i])
            sol = max(i-le +1, sol)
        return sol