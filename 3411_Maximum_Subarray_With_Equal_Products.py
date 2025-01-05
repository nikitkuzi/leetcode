class Solution:
    def maxLength(self, nums: List[int]) -> int:
        mx = 1
        n = len(nums)

        for i in range(n-1):
            product = nums[i]
            gcd_val = nums[i]
            lcm_val = nums[i]

            for j in range(i+1, n):
                product *= nums[j]
                gcd_val = gcd(gcd_val, nums[j])
                lcm_val = lcm(lcm_val, nums[j])

                if product == lcm_val * gcd_val:
                    mx = max(mx, j - i + 1)
        return mx