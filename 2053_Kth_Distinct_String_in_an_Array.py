class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        idx = 1
        seen = Counter(arr)
        n = []
        for w in arr:
            if seen[w] == 1:
                n.append(w)
        # print(n[k-1])
        return "" if k > len(n) else n[k-1]