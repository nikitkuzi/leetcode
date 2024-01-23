class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # ans = [0,0]
        # for m in moves:
        #     if m == 'U':
        #         ans[1]+=1
        #     elif m== 'D':
        #         ans[1]-=1
        #     elif m== 'L':
        #         ans[0]-=1
        #     else:
        #         ans[0]+=1
        # return ans == [0,0]
        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        return False