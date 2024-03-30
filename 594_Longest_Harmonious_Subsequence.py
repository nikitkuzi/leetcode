class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        mx = 0
        for k,v in cnt.items():
            if k+1 in cnt:
                mx = max(cnt[k+1]+v, mx)
        return mx