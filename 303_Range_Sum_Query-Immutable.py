class NumArray:

    def __init__(self, nums: List[int]):
        self.pref = []
        pre = 0
        for i in range(len(nums)):
            pre += nums[i]
            self.pref.append(pre)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pref[right]
        return self.pref[right] - self.pref[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)