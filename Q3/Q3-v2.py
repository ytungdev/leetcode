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
            # unseen char
            if char not in seen:
                seen[s[R]] = R
                R += 1
            else:
                curr = R
                # outside window, keep expanding
                if seen[char] < L:
                    R += 1
                # repeat char in window
                else:
                    L = seen[char]+1
                seen[char] = curr
            res = max(res, R-L)

        return res