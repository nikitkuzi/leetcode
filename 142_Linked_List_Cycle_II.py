# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if not head:
#             return
#         slow = head
#         fast = head
#         while fast.next and fast.next.next:
#             slow = slow.next
#             fast = fast.next.next
#             if slow == fast:
#                 slow = head
#                 while slow != fast:
#                     slow = slow.next
#                     fast = fast.next
#                 return slow
#         return None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        set_node = set()
        while curr:
            if curr not in set_node:
                set_node.add(curr)
                curr = curr.next
            else:
                return curr
        return None