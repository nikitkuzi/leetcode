class Solution:
    def countSegments(self, s: str) -> int:
        s = s.replace("  ", " ")
        return len(s.split())