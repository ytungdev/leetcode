class Solution:
    # recursion approach
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def search(ranks, cars, hi, lo):
            if hi == lo :
                return hi
            mid = (hi+lo)//2
            fixed = []
            for rank in ranks:
                n = int((mid/rank)**0.5)
                fixed.append(n)
            if sum(fixed) >= cars:
                return search(ranks, cars, mid, lo)
            else:
                return search(ranks, cars, hi, mid+1)
        hi, lo = min(ranks)*cars**2, 0
        res = search(ranks, cars, hi, lo)
        return res