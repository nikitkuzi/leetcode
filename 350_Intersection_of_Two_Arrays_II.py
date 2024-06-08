class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = Counter(nums1)
        b = Counter(nums2)
        l = []
        for i in a:
            if b.get(i) is not None:
                l+=((min(b[i],a[i]))* [i])
        return l