class Solution:
    def clearDigits(self, s: str) -> str:
        non = []
        for char in s:
            if char.isdigit():
                non.pop()
            else:
                non.append(char)
        return "".join(non)