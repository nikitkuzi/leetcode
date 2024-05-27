class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        balls = defaultdict(int)
        colors = defaultdict(int)
        cnt = 0
        ans = []
        for ball, col in queries:
            if balls[ball]:
                if colors[balls[ball]] == 1:
                    del colors[balls[ball]]
                    cnt -= 1
                else:
                    colors[balls[ball]] -= 1

            balls[ball] = col
            # if balls[ball] not in colors:
            # cnt+=1
            colors[balls[ball]] += 1

            ans.append(len(colors.keys()))
            # ans.append(cnt)
        return ans
