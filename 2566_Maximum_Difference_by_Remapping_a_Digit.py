class Solution:
    def minMaxDifference(self, num: int) -> int:
        i = 0
        n = len(str(num))
        while i < n and str(num)[i] == "9":
            i+=1
        if i == n:
            i-=1
        big = str(num).replace(str(num)[i], '9')
        i = 0

        while i < n and str(num)[i] == "0":
            i+=1
        if i == n:
            i-=1
        small = str(num).replace(str(num)[i], '0')
        # print(big, small)
        return int(big)-int(small)