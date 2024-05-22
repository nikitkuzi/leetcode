# # class Solution:

# #     def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
# #         ans = []
# #         if not n % 2: # impossible to produce even num full tree
# #             return ans
# #         # combinatorial search with backtracking, at each step either set two children or set 0 children
# #         def generate_trees(n, node, unprocessed):
# #             if n == 0:
# #                 ans.append(deepcopy(head))
# #                 return
# #             node.left = TreeNode()
# #             node.right = TreeNode()
# #             unprocessed.append(node.left)
# #             unprocessed.append(node.right)
# #             # go over every combination of dfs expansion based on unprocessed candidates
# #             for ind, next_node in enumerate(unprocessed):
# #                 generate_trees(n - 2, next_node, unprocessed[ind+1:])
# #                 next_node.left = next_node.right = None # backtrack
# #                 if n - 2 == 0: return # don't double count dups
# #         head = TreeNode()
# #         unprocessed = []
# #         generate_trees(n-1, head, unprocessed)
# #         return ans
# class Solution:
#     def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
#         #TC:O(2^n). we'll cache n mapping to list of fully binary tree it can create

#         dp = {0 : [], 1 : [TreeNode()]}   #map n : list of FBT
#         #return list of FBT
#         def backtrack(n):
#             if n in dp:
#                 return dp[n]

#             res = []
#             for l in range(n) : #0-n-1
#                 r = n - 1 -l
#                 leftTree, rightTree = backtrack(l), backtrack(r)

#                 for t1 in leftTree:
#                     for t2 in rightTree:
#                         res.append(TreeNode(0, t1, t2))
#             dp [n]= res
#             return res
#         return backtrack(n)
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:  # There can't be a full binary tree with an even number of nodes
            return []
        memo = {}

        def helper(n):
            if n in memo:
                return memo[n]

            if n == 1:
                return [TreeNode(0)]

            result = []
            for left_nodes in range(1, n, 2):  # Only odd number of nodes in the left subtree
                right_nodes = n - 1 - left_nodes
                for left in helper(left_nodes):
                    for right in helper(right_nodes):
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)

            memo[n] = result
            return result

        return helper(n)