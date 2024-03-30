class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pos = [-1]
        mx = max(nums)
        ans = 0
        for i, n in enumerate(nums):
            if n == mx:
                pos.append(i)
        if len(pos) < k:
            return 0
        if len(pos) == k:
            return 1
        for i in range(1, len(pos) - k + 1):
            l = pos[i] - pos[i - 1] - 1
            r = len(nums) - 1 - pos[i + k - 1]
            ans += (l + 1) * (r + 1)
        return ans


