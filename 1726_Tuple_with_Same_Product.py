class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        products = defaultdict(int)
        res = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                prod = nums[i]*nums[j]
                res += (products[prod]*8)
                products[prod]+=1
        return res

