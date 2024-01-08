class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L,R = 0,0
        res = 0
        seen = {}

        counter = 0             #### debug

        for R in range(len(s)):
            print(f'i:{counter:>3}, L:{L:>3}, R:{R:>3}, res:{res:>3}, sub:{s[L:R]}, seen:{seen}')
            counter+=1

            char = s[R]
            # repeated inside window, skipping L
            if seen.get(char,-1) >= L:
                L = seen[char]+1
            # update seen
            seen[char] = R

            # update max (+1 : expand window to cover next element)
            res = max(res, R-L+1)

        return res