class Solution:
    # Using counter to reduce computation of duplicated rank
    def repairCars(self, ranks: List[int], cars: int) -> int:
        hi, lo = min(ranks)*cars**2, 1
        while hi > lo:
            mid = (hi+lo)//2
            fixed = 0
            counter = Counter(ranks)
            for rank,count in counter.items():
                fixed += count * int((mid/rank)**0.5)
            if fixed >= cars:
                hi = mid
            else:
                lo = mid+1
        return hi
