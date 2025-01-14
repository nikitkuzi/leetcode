class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res = []
        curr = 0
        freq = [0] * (len(A) + 1)
        for a, b in zip(A, B):
            freq[a] += 1
            freq[b] += 1

            if freq[b] == 2:
                curr += 1
            if freq[a] == 2 and a != b:
                curr += 1

            res.append(curr)
            curr = res[-1]
        return res