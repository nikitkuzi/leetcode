class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_index = 1
        last_element = nums[0]
        for i in range(1, len(nums)):
            # print(f"i: {i}, last_element: {last_element}, last_index: {last_index}, value: {nums[i]}")
            if nums[i] != last_element:
                last_element = nums[i]
                nums[i], nums[last_index] = nums[last_index], nums[i]
                # print("swapping")
                # print(nums)
                last_index += 1
        return last_index
test = Solution()
nums = [0,1,1,1,2,2,3,3,4]
test.removeDuplicates(nums)