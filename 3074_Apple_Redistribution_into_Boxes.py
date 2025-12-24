class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        sm = sum(apple)
        res = 0
        for c in capacity:
            if sm > c:
                sm -= c
                res += 1
            else:
                res += 1
                break
        return res
