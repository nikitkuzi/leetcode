class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
#         pos = [[0 for _ in range(10)] for i in range(len(str(nums[0])))]
#         ans = 0
#         for num in nums:
#             for i, digit in enumerate(str(num)):
#                 pos[i][int(digit)]+=1
#         for i in range(len(pos)):
#             for j in range(9):
#                 for k in range(j+1,10):
#                     ans+= pos[i][j]*pos[i][k]
#         return ans
        res = 0
        div = 1
        while nums[0] // div:
            digit_counts = [0] * 10
            for num in nums:
                digit_counts[(num // div) % 10] += 1
            n = len(nums)
            for count in digit_counts:
                n -= count
                res += count * n
            div *= 10
        return res