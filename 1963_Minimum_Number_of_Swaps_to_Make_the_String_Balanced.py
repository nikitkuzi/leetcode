class Solution:
    def minSwaps(self, s: str) -> int:
        op = []
        cl = []
        for i in range(len(s)):
            if s[i] == '[':
                op.append(i)
            else:
                cl.append(i)
        co = 0
        cl = 0
        swap = 0
        for i in range(len(s)):
            if s[i] == '[':
                co += 1
            else:
                cl += 1
            if cl > co:
                swap += 1
                cl -= 1
                co += 1
                op.pop()
            if not op or i + swap > len(s):
                break
        return swap

