class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(map(lambda x: 1 if x.startswith(pref) else 0, words))