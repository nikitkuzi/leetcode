# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        ans = []
        q.append(root)
        lvl = 0
        while q:
            l = len(q)
            lvl_to_push = []

            for _ in range(l):
                node = q.popleft()
                lvl_to_push.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if lvl % 2:
                lvl_to_push.reverse()
            ans.append(lvl_to_push)
            lvl += 1
        return ans