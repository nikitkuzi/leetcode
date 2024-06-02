# class Solution:
#     def minimumDifference(self, nums: List[int], k: int) -> int:
#         res = inf
#         mask = 2**32-1

#         n = len(nums)
#         left = 0
#         count = Counter()

#         for right in range(n):

#             mask &= nums[right]

#             for idx in range(30):
#                 b = (nums[right] >> idx) & 1
#                 # record the bit count in each position
#                 if b:
#                     count[idx] += 1

#             # update the result
#             res = min(res, abs(k - mask))

#             # AND values will decrease to 0 when the size of the subarray increase
#             # if the current subarray AND is < k, we shrink the subarray
#             while mask < k:
#                 for idx in range(30):
#                     b = (nums[left] >> idx) & 1
#                     if b:
#                         count[idx] -= 1

#                     # if the current subarray has all '1' in current bit, we need to set back the AND of current bit
#                     # current subarray nums[left + 1: right + 1]
#                     # length == right - left
#                     if count[idx] == right - left:
#                         mask |= (1 << idx)
#                 # update the result
#                 res = min(res, abs(k - mask))
#                 left += 1

#         return res
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)

        # Recursive funtion with the current index and past bitwise AND value
        @cache
        def solve(idx, curr_and):
            # If index reached at the end simply pass inf
            if idx >= n:
                return inf

            # No need to check the other case since if we include curr_and it will always give us 0 value
            if curr_and & nums[idx] == 0:
                return min(abs(0 - k), abs(nums[idx] - k), solve(idx + 1, nums[idx]))

            return min(abs((curr_and & nums[idx]) - k), abs(nums[idx] - k), solve(idx + 1, nums[idx]),
                       solve(idx + 1, curr_and & nums[idx]))

        return solve(0, nums[0])