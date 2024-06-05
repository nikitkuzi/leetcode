class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = 0
        dp = [[0] * (n + 1) for _ in range(n)]
        for i in range(n - 1, -1, -1):
            suffix += piles[i]
            for m in range(1, i // 2 + 2):
                if i + m * 2 >= n:  # Take all
                    dp[i][m] = suffix
                else:
                    dp[i][m] = suffix - min(dp[i + x][max(m, x)] for x in range(1, m * 2 + 1))
        return dp[0][1]
# class Solution:
#     def stoneGameII(self, piles: List[int]) -> int:

# 		# Constants
#         ALICE = 1 # To represent current turn.
#         BOB = -1 # To represent current turn.
#         N = len(piles)

# 		# Helpers
#         @cache
#         def max_piles_from(idx, m, turn): # Returns alice's gain from the given state.
#             if idx == N:
#                 return 0

#             # Note: We need to maximize alice's gain in alice's turn, minimize alice's gain in bob's turn.
#             localMax = 0
#             localMin = float('inf')
#             turnSum = 0

# 			# Try all choices.
#             for x in range(1, min(2*m, N-idx) + 1): # harvesting index's upper is N-1.
#                 harvesting_idx = idx + x - 1
#                 turnSum += piles[harvesting_idx]
#                 next_m = max(m, x)

#                 current_turn_gain = turnSum if turn == ALICE else 0
#                 future_gain = max_piles_from(harvesting_idx+1, next_m, -turn) # Switching turn by multipling -1.

#                 localMax = max(localMax, current_turn_gain + future_gain)
#                 localMin = min(localMin, current_turn_gain + future_gain)

#             return localMax if turn == ALICE else localMin

#         # Main
#         return max_piles_from(0, 1, ALICE)