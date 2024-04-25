class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def f(node, path):
            if not node.left and not node.right:
                ans.append(path+str(node.val))
                return
            if node.left:
                f(node.left, path+str(node.val)+"->")
            if node.right:
                f(node.right, path+str(node.val)+"->")
        f(root, "")
        return ans