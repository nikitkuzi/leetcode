class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d = defaultdict(deque)
        l = 0
        mx = 0
        for i, char in enumerate(s):
            d[char].append(i)
            if len(d[char])>2:
                if l < d[char][0]+1:
                    l = d[char][0]+1
                d[char].popleft()
            mx = max(mx, i-l+1)
        return mx
