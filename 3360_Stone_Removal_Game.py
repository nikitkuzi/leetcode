class Solution:
    def canAliceWin(self, n: int) -> bool:
        sub = 10
        alice = False
        while n-sub>=0:
            n-=sub
            sub-=1
            alice^=1
        return True if alice else False