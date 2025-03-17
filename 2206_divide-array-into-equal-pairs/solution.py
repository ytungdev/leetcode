class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1

        for count in counter.values():
            if count % 2 != 0:
                return False
        return True
        # return all(count % 2 == 0 for count in counter.values())