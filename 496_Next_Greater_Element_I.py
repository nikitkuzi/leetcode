class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = defaultdict(int)
        q = []
        for i in range(len(nums2)-1, -1, -1):
            while q and q[-1] < nums2[i]:
                    q.pop()
            if not q:
                d[nums2[i]] = -1
            else:
                d[nums2[i]] = q[-1]
            q.append(nums2[i])
        res = []
        for n in nums1:
            res.append(d[n])
        return res