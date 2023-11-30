# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        inorder = []
        lvl = []

        def f(root, h):
            if not root:
                return None
            f(root.left, h + 1)
            inorder.append(root.val)
            lvl.append(h)
            f(root.right, h + 1)

        f(root, 0)
        p_idx = inorder.index(p.val)
        q_idx = inorder.index(q.val)
        print(inorder)
        print(lvl)
        if p_idx > q_idx:
            p_idx, q_idx = q_idx, p_idx
        LCA = 10 ** 6
        mn_idx = 0
        for i in range(p_idx, q_idx + 1):
            if LCA > lvl[i]:
                mn_idx = i
                LCA = lvl[i]
        print(mn_idx)
        LCA = inorder[mn_idx]
        print(LCA)
        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.val == LCA:
                return node

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)



