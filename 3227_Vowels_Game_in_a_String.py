class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = 0
        for char in s:
            if char in "aeiuo":
                return True
        return False