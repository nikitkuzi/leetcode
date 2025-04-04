# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node, depth):
            if not node.left and not node.right:
                return node, depth

            left, l_depth = dfs(node.left, depth + 1) if node.left else (node, depth)
            right, r_depth = dfs(node.right, depth + 1) if node.right else (node, depth)

            if l_depth == r_depth:
                return node, l_depth

            return (left, l_depth) if l_depth > r_depth else (right, r_depth)

        lca, _ = dfs(root, 0)
        return lca
# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         h = 0
#         ch = []
#         def f(root, depth):
#             if not root.left and not root.right:
#                 nonlocal h
#                 nonlocal ch
#                 if h < depth:
#                     h = depth
#                     ch = [root.val]
#                 elif h == depth:
#                     ch.append(root.val)
#             if root.left:
#                 f(root.left, depth+1)
#             if root.right:
#                 f(root.right, depth+1)
#         f(root, 0)
#         if len(ch) == 1:
#             return TreeNode(ch[0])
#         ch = set(ch)
#         ans = -1
#         # print(ch, h)
#         def g(root):
#             if not root:
#                 return 0
#             if not root.left and not root.right:
#                 return 1 if root.val in ch else 0
#             l = g(root.left)
#             r = g(root.right)
#             # print(l+r)
#             if l and r and l+r == len(ch):
#                 nonlocal ans
#                 ans = root

#             return l+r
#         g(root)
#         return ans
