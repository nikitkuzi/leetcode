class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        q = deque()
        for i, s in enumerate(skills):
            q.append((s,i))
        v1 = 0
        v2 = 0
        p1 = q.popleft()
        p2 = q.popleft()
        if k>len(skills):
            return skills.index(max(skills))
        while v1 < k and v2 < k:
            if p1[0]>p2[0]:
                v1+=1
                v2=0
                q.append(p2)
                p2=q.popleft()
            else:
                v2+=1
                v1=0
                q.append(p1)
                p1 = q.popleft()
        # print(p1[1], p2[1])
        return p1[1] if v1>v2 else p2[1]

