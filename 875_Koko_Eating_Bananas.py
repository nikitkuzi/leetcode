class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sm = sum(piles)
        if h>sm:
            return 1
        piles.sort()
        l = ceil(sm/h)
        r = piles[-1]

        while l<=r:
            mid = (l+r)//2
            k = 0
            for p in piles:
                if k>h:
                    break
                k+= ceil(p/mid)
            # print(l,r,mid,k)
            if k <= h:
                r = mid-1
            elif k > h:
                l = mid+1
            # else:
            #     return mid
        return l