class Solution:
    # while-loop approach
    def repairCars(self, ranks: List[int], cars: int) -> int:
        hi, lo = min(ranks)*cars**2, 1
        while hi >= lo:
            if hi == lo:
                return hi
            mid = (hi+lo)//2
            fixed = 0
            for rank in ranks:
                fixed += int((mid/rank)**0.5)
            if fixed >= cars:
                hi = mid
            else:
                lo = mid+1
