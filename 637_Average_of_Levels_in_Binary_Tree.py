# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:

        avg = defaultdict(list)

        def f(root, lvl):
            if not root:
                return None
            avg[lvl].append(root.val)
            # avg[lvl][1] += 1
            if root.left:
                f(root.left, lvl + 1)
            if root.right:
                f(root.right, lvl + 1)

        f(root, 0)
        return [sum(v) / len(v) for k, v in avg.items()]  