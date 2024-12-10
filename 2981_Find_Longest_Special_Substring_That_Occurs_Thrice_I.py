class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        curr = s[0]
        d[curr]+=1
        for i in range(1, len(s)):
            if s[i] == curr[0]:
                curr += s[i]
            else:
                curr = s[i]
            for j in range(1,len(curr)+1):
                d[curr[:j]] += 1
        # print(d)
        l = [len(k) for k, v in d.items() if v >= 3]
        # l.sort()
        if l:
            return max(l)
        return -1
