class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        seen = defaultdict(int)
        mx = -1
        for num in nums:
            sm = get_digit_sum(num)
            if sm in seen:
                mx = max(num + seen[sm], mx)
            seen[sm] = max(num, seen[sm])
        return mx