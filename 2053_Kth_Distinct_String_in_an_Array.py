class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        idx = 1
        seen = Counter(arr)
        n = []
        for w in arr:
            if seen[w] == 1:
                n.append(w)
            if len(n) == k:
                return w
        return ""