class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
            res = []
            l,r = 0,1
            used = nums[l]
            ans = 1
            while l<r and r<len(nums):
                if nums[r]&used == 0:
                    used+=nums[r]
                    ans+=1
                    r+=1
                else:
                    res.append(ans)
                    l+=1
                    r=l+1
                    used = nums[l]
                    ans=1
            res.append(ans)
            return max(res)