class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s = set(arr)
        res = 0
        def f(a, b, curr):
            if a+b in s:
                a, b = b, a+b
                curr+=1
                nonlocal res
                res = max(res, curr)
                f(a,b, curr)
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1, n):
                f(arr[i], arr[j], 2)
        return res