class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        ans=0
        for n in nums:
            if d[k-n]> 0:
                d[k-n]-=1
                ans+=1
                continue
            d[n]+=1
        return ans