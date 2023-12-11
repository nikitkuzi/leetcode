class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def f(curr, left):
            # print(curr,left)
            if not left:
                ans.append(curr)
                return
            for i in range(len(left)):
                f(curr + [left[i]], left[:i] + left[i + 1:])

        for i in range(len(nums)):
            f([nums[i]], nums[:i] + nums[i + 1:])

        return ans