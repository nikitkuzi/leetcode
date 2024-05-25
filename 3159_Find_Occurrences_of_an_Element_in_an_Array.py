class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        d = defaultdict(list)
        ans = []
        for i,n in enumerate(nums):
            d[n].append(i)
        for q in queries:
            if q > len(d[x]):
                ans.append(-1)
            else:
                ans.append(d[x][q-1])
        return ans