class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        l = 0
        r = len(numbers) - 1
        while numbers[l] + numbers[r]!= target:
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1
        return [l+1, r+1]

test = Solution()
numbers = [2,7,11,15]
target = 9
numbers = [2,3,4]
target = 6
numbers = [-1,0]
target = -1
print(test.twoSum(numbers,target))

