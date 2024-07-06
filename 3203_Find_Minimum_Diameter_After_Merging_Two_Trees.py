class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def getDiameter(edges):
            map = defaultdict(list)
            for i, j in edges:
                map[i].append(j)
                map[j].append(i)

            res = [0]

            def dfs(node, parent):
                maxDepth = 1
                for neighbor in map[node]:
                    if neighbor == parent:
                        continue
                    depth = dfs(neighbor, node)
                    res[0] = max(res[0], maxDepth + depth)
                    maxDepth = max(maxDepth, 1 + depth)
                return maxDepth

            dfs(0, -1)

            return res[0]

        d1 = getDiameter(edges1)
        d2 = getDiameter(edges2)

        return max(d1 - 1, d2 - 1, d1 // 2 + d2 // 2 + 1)