class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1:
            return [1]
        res = [0] * (2 * n)
        res[1] = n
        res[n + 1] = n
        used = [0] * (n + 1)
        used[n] = 1
        ans = [0]

        def f(curr_pos):
            # print(curr_pos, res, used)
            if curr_pos == 2 * n:
                # print("here")
                nonlocal ans
                if ans[0] == 0:
                    ans = res[1:]
                return True

            if res[curr_pos] != 0:
                return f(curr_pos + 1)

            for num in range(n, 0, -1):
                if not used[num]:
                    if num == 1:
                        if res[curr_pos] == 0:
                            res[curr_pos] = 1
                            used[num] = 1
                            if f(curr_pos + 1):
                                return True
                            res[curr_pos] = 0
                            used[num] = 0
                    else:
                        if res[curr_pos] == 0 and curr_pos + num + 1 <= 2 * n and res[num + curr_pos] == 0:
                            used[num] = 1
                            res[curr_pos] = num
                            res[curr_pos + num] = num
                            if f(curr_pos + 1):
                                return True
                            used[num] = 0
                            res[curr_pos] = 0
                            res[curr_pos + num] = 0
            return False

        f(2)
        return ans
