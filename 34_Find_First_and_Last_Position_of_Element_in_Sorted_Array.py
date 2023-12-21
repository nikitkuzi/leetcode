class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bin_search(left_bias):
            l, r = 0, len(nums) - 1
            i = -1

            while (l <= r):
                mid = (l + r) // 2

                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    i = mid
                    if left_bias:
                        r = mid - 1
                    else:
                        l = mid + 1

            return i

        l = bin_search(True)
        r = bin_search(False)

        return [l, r]