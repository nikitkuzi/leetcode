class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        # res = 1
        # for n in derived:
        #     res ^= n
        # return res == 1
        return sum(derived) % 2 == 0