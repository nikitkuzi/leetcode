class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)
        s = sorted(cnt.values(), reverse = True)
        res = 0
        curr = 2
        cycle = 1
        for n in s:
            res += n*cycle
            curr+=1
            if curr == 10:
                curr = 2
                cycle += 1
        return res