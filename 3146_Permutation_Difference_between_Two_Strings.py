class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        pos1 = [0] * 26
        pos2 = [0] * 26

        for i in range(len(s)):
            pos1[ord(s[i]) - 97] = i
            pos2[ord(t[i]) - 97] = i

        return sum(abs(i - j) for i, j in zip(pos1, pos2))