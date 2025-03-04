class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        s = ""
        while n:
            s+= str(n%3)
            n//=3
        # print(s)
        return s.count('2')==0