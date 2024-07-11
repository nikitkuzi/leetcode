class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new = sorted(score, reverse = True)
        ranks = {new[i]:i+1 for i in range(len(new))}
        ans = []
        for s in score:
            if ranks[s] == 1:
                ans.append("Gold Medal")
            elif ranks[s] == 2:
                ans.append("Silver Medal")
            elif ranks[s] == 3:
                ans.append("Bronze Medal")
            else:
                ans.append(str(ranks[s]))
        return ans