class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        seen = set()
        for i in range(len(nums) - 1,  -1, -1):
            if nums[i] in seen:
                return i // 3 + 1
            seen.add(nums[i])
        return 0
        # c = defaultdict(list)
        # for i, n in enumerate(nums):
        #     c[n].append(i)
        # mx = -1
        # for num in c.keys():
        #     if len(c[num])>1:
        #         mx = max(mx, c[num][-2])
        # # print(mx)
        # return (mx) // 3+1