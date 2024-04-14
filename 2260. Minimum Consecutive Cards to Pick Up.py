class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # c = set(cards)
        # seen = defaultdict(int)
        seen = {}
        mn = float(inf)
        for i in range(len(cards)):
            if cards[i] in seen:
                mn = min(mn, i-seen[cards[i]]+1)
            seen[cards[i]] = i
            # else:
                # seen[cards[i]] = i
        return -1 if mn == float(inf) else mn