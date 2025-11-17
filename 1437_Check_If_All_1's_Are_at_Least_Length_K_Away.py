class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        ones = []
        for i, n in enumerate(nums):
            if n == 1:
                if not ones:
                    ones.append(i)
                    continue
                if i - ones[-1]-1 < k:
                    return False
                else:
                    ones.append(i)
        return True