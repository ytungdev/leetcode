class Solution:

    cases = [
        ('babad', 'bab'),
        ('cbbd', 'bb'),
        ('a', 'a'),
        ('','')
    ]

    def test_all(self):
        for case in self.cases:
            ans = self.longestPalindrome(case[0])
            print(f'ans : {ans}, exp:{case[1]}')

    def test(self,n):
        ans = self.longestPalindrome(self.cases[n][0])
        print(f'ans : {ans}, exp:{self.cases[n][1]}')


    def longestPalindrome(self, s: str) -> str:
        # eliminate even len
        s = "#"+"#".join(s)+"#"
        print(s)
        longest    = ""
        longestLen = 0
        for i in range(len(s)):
            L,R = i,i
            while L>=0 and R<len(s) and s[L] == s[R]:
                print(f'L:{L}, R:{R}, s:{s[L:R+1]}, s:{s[L:R]}')
                currLen = (R-L+1)
                if currLen > longestLen:
                    longestLen = currLen
                    longest = s[L:R+1]
                L -= 1
                R += 1

        return "".join([c for c in longest if c!='#'])

if __name__ == '__main__':
    solution = Solution()
    solution.test(1)