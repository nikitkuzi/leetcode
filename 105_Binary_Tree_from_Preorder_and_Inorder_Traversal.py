# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        root_index = inorder.index(root)
        root.left = self.buildTree(preorder[1:root_index+1], inorder[:root_index])
        root.right = self.buildTree(preorder[root_index:], inorder[root_index:])
        return root


        # root = preorder[0]
        # root_pos = inorder.index(root)
        # visited = set()
        # inorder = [[i, element] for i, element in enumerate(inorder)]
        #
        # def buildNode(node, unordered, visited):
        #     l, r = None, None
        #     for elem in unordered:
        #         if elem == root:
        #
        #             pass


test = Solution()
preorder = [3,9,4,1,5,20,15,7]
inorder = [1,4,9,5,3,15,20,7]
print(test.buildTree(preorder, inorder))