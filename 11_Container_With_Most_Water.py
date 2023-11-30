class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        max_height = max(height)
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if max_area >= max_height * (right - left):
                break

        return max_area


test = Solution()
# height = [1, 1]
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# height = [2,3,4,5,18,17,6]
height = [1,2,3,4,5,25,24,3,4]

print(test.maxArea(height))
