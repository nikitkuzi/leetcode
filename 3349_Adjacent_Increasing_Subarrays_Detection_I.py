class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        tmp = [1]
        pos = []
        n = len(nums)
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                tmp.append(tmp[-1] + 1)
            else:

                tmp.append(1)
            if tmp[-1] >= k:
                pos.append(i)

        # print(tmp)
        # print(pos)
        for p in pos:
            if p < n - k and tmp[p] >= k and tmp[p + k] >= k:
                return True
        return False
