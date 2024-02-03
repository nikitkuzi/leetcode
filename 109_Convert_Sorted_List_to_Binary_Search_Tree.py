# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def build(root):
            if not root:
                return
            new_node = TreeNode()
            new_node.left = build(root[:len(root) // 2])
            new_node.val = root[len(root) // 2]
            new_node.right = build(root[len(root) // 2 + 1:])
            return new_node

        if not head:
            return
        if not head.next:
            return TreeNode(head.val)
        root = []
        curr = head
        while curr:
            root.append(curr.val)
            curr = curr.next

        ans = TreeNode()
        ans.left = build(root[:len(root) // 2])
        ans.val = root[len(root) // 2]
        ans.right = build(root[len(root) // 2 + 1:])
        return ans

