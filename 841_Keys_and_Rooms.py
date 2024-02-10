class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False]*len(rooms)
        visited[0] = True
        q = deque()
        q.append(rooms[0])
        while q:
            cur_keys = q.popleft()
            for key in cur_keys:
                if not visited[key]:
                    q.append(rooms[key])
                    visited[key] = True
        return all(visited)