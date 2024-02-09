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


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def dfs(node, left, right):
            count = max(left, right)

            if node.left:
                count = max(count, dfs(node.left, right + 1, 0))

            if node.right:
                count = max(count, dfs(node.right, 0, left + 1))
            return count

        return dfs(root, 0, 0)