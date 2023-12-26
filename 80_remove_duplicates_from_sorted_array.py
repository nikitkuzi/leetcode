class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        last_index = 1
        last_element = nums[0]
        unique_count = 1
        for i in range(1, len(nums)):
            if nums[i] == last_element and unique_count == 1:
                # print("first duplicate")
                nums[i], nums[last_index] = nums[last_index], nums[i]
                unique_count += 1
                last_index += 1
                continue
            # print(f"i: {i}, last_element: {last_element}, last_index: {last_index}, value: {nums[i]}")
            if nums[i] != last_element and unique_count <= 2:
                last_element = nums[i]
                nums[i], nums[last_index] = nums[last_index], nums[i]
                # print("swapping")
                # print(nums)
                last_index += 1
                unique_count = 1
            

        return last_index
test = Solution()
nums = [0,0,1,1,1,1,2,3,3]
test.removeDuplicates(nums)