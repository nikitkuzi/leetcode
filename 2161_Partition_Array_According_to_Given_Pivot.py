class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        e = []
        r = []
        for n in nums:
            if n < pivot:
                l.append(n)
            elif n > pivot:
                r.append(n)
            else:
                e.append(n)
        return l+e+r