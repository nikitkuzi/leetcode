class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sm = 0
        def f(i, curr, sm):
            print(i, curr, sm)
            if sm > target:
                return
            if sm == target:
                res.append(tuple(curr))
                return
            for j in range(i+1, len(candidates)):
                curr.append(candidates[j])
                f(j, curr, sm+candidates[j])
                curr.pop()
        for i in range(len(candidates)):
            f(i, [candidates[i]], candidates[i])
        # print(res)
        return [list(x) for x in set(res)]