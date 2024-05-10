class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        cnt = defaultdict(int)
        n = len(nums)
        heap = []
        res = [0] * n
        for i, (v, f) in enumerate(zip(nums, freq)):
            cnt[v] += f
            heapq.heappush(heap, [-cnt[v], v])
            while heap and -heap[0][0] != cnt[heap[0][1]]:
                heapq.heappop(heap)
            if heap:
                res[i] = -heap[0][0]
        return res