class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num += 2**32
        hex_c = "0123456789abcdef"
        s=""
        while(num>0):
            s = hex_c[num%16] + s
            num//=16
        return s