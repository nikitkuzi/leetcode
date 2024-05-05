class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        subs = [word[i:i+k] for i in range(0, len(word),k)]
        # print(subs)
        ans = 0
        ans = len(subs) - Counter(subs).most_common(1)[0][1]
        return ans