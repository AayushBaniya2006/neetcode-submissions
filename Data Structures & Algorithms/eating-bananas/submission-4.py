class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)

        while l <= r:
            
            mid = (l+r) // 2
            print(mid)
            holder = self.checker(mid,piles,h)
            if holder == -1:
                l = mid + 1
            elif holder == 1: 
                r = mid - 1
        return l 
    def checker(self, mid,piles, h):
        curr = 0
        for i in piles:
            curr += math.ceil(i/mid)
            if curr > h: 
                return -1 
        print(curr)
        print(" ")
        return 1
