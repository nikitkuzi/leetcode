class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)
        l = 0
        r = 0
        ones = 0
        zeros = deque()
        mx = 0
        while r < len(nums):
            while nums[r] == 1:
                r+=1
                ones+=1
                if r == len(nums):
                    mx = max(mx,min(ones+k,len(nums)))
                    return mx
            if nums[r] == 0:
                if len(zeros) == k:
                    mx = max(mx,ones+k)
                    if zeros:
                        ones -= (zeros[0]-l)
                        l = zeros.popleft()+1
                if k > 0:
                    zeros.append(r)
                else:
                    ones = 0
            r+=1
        if ones+k >= len(nums):
            mx = len(nums)
        return mx