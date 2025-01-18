class Solution:
    def minCost(self, arr: List[int], brr: List[int], k: int) -> int:
        res = 0
        for a,b in zip(arr,brr):
            res += abs(a-b)
        mn = res
        arr.sort()
        brr.sort()
        res = 0
        for a,b in zip(arr,brr):
            res += abs(a-b)
        mn = min(mn, res+k)
        return mn
