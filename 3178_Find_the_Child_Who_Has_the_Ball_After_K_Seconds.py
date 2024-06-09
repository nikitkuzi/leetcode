class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        if k<n:
            return k
        forwrd = (k//(n-1))%2==0
        k%=(n-1)
        # print(forwrd, k, n-k-1)
        if forwrd:
            return k
        else:
            return n-k-1