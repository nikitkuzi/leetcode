class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.mx = 0

        def dfs(node, left, right):
            self.mx = max(self.mx, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)

            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)
        return self.mx