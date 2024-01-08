class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R = 0,0
        res = 0

        while R < len(s):
            if s[R] not in s[L:R]:
                R += 1
            else:
                L += 1
            res = max(res, R-L)

        return res