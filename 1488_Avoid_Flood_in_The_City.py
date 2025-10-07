class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        h   = {}
        q   = deque([])
        res = []
        for i, x in enumerate(rains):
            if x:
                if x in h:
                    for j in q:
                        if j > h[x]:
                            res[j] = x
                            q.remove(j)
                            break
                    else:
                        return []
                res.append(-1)
                h[x] = i
            else:
                res.append(1)
                q.append(i)
        return res