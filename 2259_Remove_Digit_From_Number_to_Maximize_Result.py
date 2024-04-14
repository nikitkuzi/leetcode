class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        nums = []
        for i in range(len(number)):
            if number[i] == digit:
                nums.append(number[:i]+number[i+1:])
        # print(nums)
        return(sorted(nums)[-1])