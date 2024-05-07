class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        def f(num, operation):
            for i in range(31, -1, -1):
                if operation == '+':
                    bits[i] += num & 1
                else:
                    bits[i] -= num & 1
                num >>= 1
                if num == 0:
                    return

        def convert(bits):
            num = 0
            for i in range(32):
                if bits[i] > 0:
                    num += 2 ** (31 - i)
            return num

        total = 0
        l = 0
        mn = inf
        bits = [0] * 32
        for r in range(len(nums)):
            # convert = nums[r]
            f(nums[r], '+')
            # for i in range(31,-1,-1):
            #     bits[i]+=convert&1
            #     convert >>= 1
            #     if convert == 0:
            #         break
            # print(bits)

            total |= nums[r]
            while l < r:
                if total < k:
                    break
                else:
                    mn = min(mn, r - l + 1)
                    # total -= nums[l]
                    f(nums[l], '-')
                    total = convert(bits)
                    l += 1
            if l == r and total >= k:
                return 1

        return -1 if mn == inf else mn

