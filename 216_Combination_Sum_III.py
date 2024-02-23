# class Solution:
#     def combinationSum3(self, k: int, n: int) -> List[List[int]]:
#         res = []

#         def backtrack(num, stack, target):
#             if len(stack) == k:
#                 if target == 0:
#                     res.append(stack)
#                 return

#             for x in range(num + 1, 10):
#                 if x <= target:
#                     backtrack(x, stack + [x], target - x)
#                 else:
#                     return

#         backtrack(0, [], n)
#         return res
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i + 1)
                backtrack(remain - i - 1, comb, i + 1)
                # backtrack the current choice
                comb.pop()

        # If we started the backtrack function directly from 1, we'd be assuming the first number to always be part of our combination
        backtrack(n, [], 0)

        return results