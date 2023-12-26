class Solution:
    # keep order, probably bad
    def removeElement(self, nums: List[int], val: int) -> int:
        last_indexes = [idx for idx, v in enumerate(nums) if v == val]
        ans = len(nums) - len(last_indexes)
        if not last_indexes:
            return len(nums)
        last_index = last_indexes.pop()
        last_element = True if not last_indexes else False

        for i in range(len(nums) - 1, -1, -1):
            if i != last_index:
                nums[i], nums[last_index] = nums[last_index], nums[i]
                if last_element:
                    break
                last_index = last_indexes.pop()
                if not last_indexes:
                    last_element = True
            else:
                if last_element:
                    break
                last_index = last_indexes.pop()
                if not last_indexes:
                    last_element = True           
        return ans

        # dont keep order
        # def removeElement(self, nums: List[int], val: int) -> int:
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != val:
        #         nums[index] = nums[i]
        #         index += 1
        # return index
test = Solution()
nums = [0,1,2,2,3,0,4,2]
val = 2
print(test.removeElement(nums, val))