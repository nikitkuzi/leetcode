class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        rem = defaultdict(int)
        for n in nums:
            rem[n%value]+=1
        for i in range(len(nums)):
            if rem[i%value] == 0:
                return i
            else:
                rem[i%value]-=1
        return i+1