class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        ar = [[] for i in range(101)]
        for n in nums:
            ar[len(n)].append(n)
        numbers = []
        while k>0:
            numbers = ar.pop()
            k-= len(numbers)
        if k < 0:
            k+=len(numbers)
        return sorted(numbers)[-k]