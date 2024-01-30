class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for a in asteroids:
            while ans and ans[-1] *a< 0:
                if ans[-1] > 0:
                    if ans[-1]>abs(a):
                        break
                    elif ans[-1] == abs(a):
                        ans.pop()
                        break
                    elif ans:
                        ans.pop()
                    # else:
                        # break
                else:
                    ans.append(a)
                    break
            else:
                ans.append(a)
        return ans