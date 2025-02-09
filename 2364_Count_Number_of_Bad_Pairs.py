class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        diffs = defaultdict(int)
        res = 0
        for i, n in enumerate(nums):
            curr_diff = i-n
            res += diffs[curr_diff]
            diffs[curr_diff]+=1
        return (len(nums) * (len(nums)-1)) // 2 - res