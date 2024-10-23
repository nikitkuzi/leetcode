# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        sms = []
        sm = 0
        lvl = 0
        while q:
            lvl_len = len(q)
            sm = 0
            for i in range(lvl_len):
                curr = q.popleft()
                sm += curr.val
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            sms.append(sm)
        sms.append(0)
        q.append(root)
        lvl = 0
        while q:
            lvl_len = len(q)
            lvl += 1
            for i in range(lvl_len):
                curr = q.popleft()
                # print(lvl,sms[lvl], curr)
                # print(curr.left)
                # print(curr.right)
                # print()
                if curr.left and curr.right:
                    curr.left.val, curr.right.val = sms[lvl] - curr.right.val - curr.left.val, sms[
                        lvl] - curr.left.val - curr.right.val
                    q.append(curr.left)
                    q.append(curr.right)
                elif curr.left:
                    curr.left.val = sms[lvl] - curr.left.val
                    q.append(curr.left)
                elif curr.right:
                    curr.right.val = sms[lvl] - curr.right.val
                    q.append(curr.right)
        root.val = 0
        # print(root)
        return root





