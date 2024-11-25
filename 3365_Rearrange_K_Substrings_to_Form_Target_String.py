class Solution:
    def isPossibleToRearrange(self, s: str, t: str, k: int) -> bool:
        if len(s) == k:
            return Counter(s) == Counter(t)
        sbstr = len(s) // k
        if len(s) % k:
            return False

        s1 = [s[i * sbstr:(i + 1) * sbstr] for i in range(k)]
        s2 = [t[i * sbstr:(i + 1) * sbstr] for i in range(k)]

        return Counter(s1) == Counter(s2)

