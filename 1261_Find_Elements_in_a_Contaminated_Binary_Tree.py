# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.seen = set()
        self.build(0, self.root)

    def build(self, val, node):
        node.val = val
        self.seen.add(val)
        l = node.left
        r = node.right
        if l:
            self.build(val * 2 + 1, l)
        if r:
            self.build(val * 2 + 2, r)

    def find(self, target: int) -> bool:
        return target in self.seen

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)