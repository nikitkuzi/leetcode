class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        sm = 0
        def f(i, curr, sm):
            # print(i, curr, sm)
            if sm > target:
                return
            if sm == target:
                res.add(tuple(curr))
                return
            for j in range(i+1, len(candidates)):
                if j > i+1 and candidates[j] == candidates[j-1]:
                    continue
                # curr.append(candidates[j])
                if candidates[j]+sm > target:
                    break
                f(j, curr+[candidates[j]], sm+candidates[j])
                # curr.pop()
        for i in range(len(candidates)):
            f(i, [candidates[i]], candidates[i])
        # print(res)
        return res