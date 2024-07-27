class Solution:
    def doesAliceWin(self, s: str) -> bool:
        c = 0
        for char in s:
            if char in "aeiuo":
                c+=1
        if c>0:
            return True
        else:
            return False