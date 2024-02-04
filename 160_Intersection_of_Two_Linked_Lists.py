# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def l(head):
            # dummy = ListNode()
            # dummy.next = head
            # prev = dummy
            curr = head
            n = 0
            while curr:
                n += 1
                curr = curr.next
            return n

        n = l(headA)
        m = l(headB)
        if n > m:
            headA, headB = headB, headA
            n, m = m, n
        # print(headA)
        # print(headB)
        while n != m:
            headB = headB.next
            m -= 1

        while headA and headA != headB:
            headA = headA.next
            headB = headB.next
        # print(headA)
        # print(headB)
        return None if not headA else headA



