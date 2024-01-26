class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3: return False
        Check = [math.inf,math.inf]
        for num in nums:
            if num <= Check[0]:
                Check[0] = num
            elif num <= Check[1]:
                Check[1] = num
            else:
                return True
        return False