class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2)
        h = [(nums1[0] + nums2[0], 0, 0)] #store (nums1[i] + nums2[j], i, j)
        res = []
        while h and len(res) < k:
            s, i, j = heapq.heappop(h)
            res.append([nums1[i],nums2[j]])

            if i + 1 < n1:
                heapq.heappush(h, (nums1[i+1] + nums2[j], i+1, j))
            if i == 0 and j + 1 < n2:#to avoid repeation
                heapq.heappush(h, (nums1[i] + nums2[j+1], i, j+1))

        return res