class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for l in nums1:
            for r in nums2:
                if l%(r*k)==0:
                    ans+=1
        return ans