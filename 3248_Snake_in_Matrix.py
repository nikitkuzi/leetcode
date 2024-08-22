class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        moves = {"RIGHT":(0, 1), "LEFT":(-1, 0), "DOWN":(1, 0), "UP":(-1, 0)}
        x,y = 0, 0
        for command in commands:
            dx, dy = moves[command]
            x += dx
            y += dy
        return (x * n) + y