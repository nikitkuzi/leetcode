class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n = len(s)
        k = k % n
        result = ""
        for i in range(n):
            result += s[(i + k) % n]
        return result