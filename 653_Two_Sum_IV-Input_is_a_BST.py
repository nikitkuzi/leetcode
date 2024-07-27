class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()
        def find(node):
            if node is None:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return find(node.left) or find(node.right)
        return find(root)