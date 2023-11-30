# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.inorder = deque()
        self.mn = 10**6
        def to_inorder(root):
            if not root:
                return Noneg
            to_inorder(root.left)
            self.inorder.append(root.val)
            self.mn = min(self.mn, root.val)
            to_inorder(root.right)
        to_inorder(root)
        self.mn_idx = self.inorder.index(self.mn)
        for _ in range(self.mn_idx):
            self.inorder.popleft()
        self.node_count = len(self.inorder)

    def next(self) -> int:
        return self.inorder.popleft()

    def hasNext(self) -> bool:
        return True if self.inorder else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()