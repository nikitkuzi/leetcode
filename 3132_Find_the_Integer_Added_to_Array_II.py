class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        min2 = min(nums2)
        a, b, c = [min2 - val for val in heapq.nsmallest(3, nums1)]

        ans = float(inf)
        for x in (a, b, c):
            nums2 = Counter(nums2)
            target = Counter(val + x for val in nums1)
            f = True
            for k, v in nums2.items():
                if k not in target or v > target[k]:
                    f = False
                    break
            if f:
                ans = min(ans, x)
        return ans