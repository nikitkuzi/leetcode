class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        score = 0

        for num, idx in sorted_nums:
            if nums[idx] != -1:  # Process only if not already marked
                score += num
                nums[idx] = -1  # Mark current index
                if idx > 0:
                    nums[idx - 1] = -1  # Mark left neighbor
                if idx < n - 1:
                    nums[idx + 1] = -1  # Mark right neighbor

        return score

# class Solution:
#     def findScore(self, nums: List[int]) -> int:
#         marked = [False]*len(nums)
#         score = 0
#         h = []
#         for i, n in enumerate(nums):
#             heapq.heappush(h, (n, i))
#         while h:
#             n, i = heapq.heappop(h)
#             if not marked[i]:
#                 score += n
#                 marked[i] = True
#                 if i > 0:
#                     marked[i-1] = True
#                 if i < len(nums)-1:
#                     marked[i+1] = True
#         return score