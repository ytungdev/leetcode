class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)-2):
            compliment = 0 - nums[i]
            L,R = i+1,len(nums)-1
            while L<R:
                total = nums[L]+nums[R]
                if total == compliment:
                    ans.add((nums[i], nums[L], nums[R]))
                if total > compliment:
                    R -= 1
                else:
                    L += 1
        return ans