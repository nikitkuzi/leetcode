class Solution:
    def intToRoman(self, num: int) -> str:
        # Creating Dictionary for Lookup
        num_map = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX",
                   5: "V", 4: "IV", 1: "I"}

        # Result Variable
        r = ''

        # for n in num_map.keys[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
        for n in num_map.keys():
            # If n in list then add the roman value to result variable
            while n <= num:
                r += num_map[n]
                num -= n
        return r