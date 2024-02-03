# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = ListNode(float(-inf))

        def f(node, s):
            if s.val == float(-inf):
                return ListNode(node.val)
            if node.val < s.val:
                return ListNode(node.val, s)
            dummy = ListNode()
            dummy.next = s
            curr = s
            prev = dummy
            while curr:
                # print(curr.val,node.val)
                if curr.val > node.val:
                    n = ListNode(node.val)
                    n.next = curr
                    prev.next = n
                    return dummy.next
                else:
                    prev, curr = curr, curr.next
            prev.next = ListNode(node.val)
            return dummy.next

        curr = head
        while curr:
            s = f(curr, s)
            curr = curr.next
        return s