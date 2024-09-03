class Solution:
    def getLucky(self, s: str, k: int) -> int:
        st = "".join([str(ord(char)-96) for char in s])
        while k:
            st = str(sum([int(char) for char in st]))
            k-=1
        return int(st)