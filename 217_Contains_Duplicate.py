class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        occurence_dict = {}
        for num in nums:
            if occurence_dict.get(num, ""):
                return True
            else:
                occurence_dict[num] = 1
        return False
