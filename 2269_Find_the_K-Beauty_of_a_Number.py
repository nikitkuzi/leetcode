class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        for i in range(len(str(num))-k+1):
            if int(str(num)[i:i+k])  and num % int(str(num)[i:i+k]) == 0:
                ans+=1
        return ans