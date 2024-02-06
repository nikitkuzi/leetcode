# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        m1 = 0
        n1 = 0
        count = m * n
        steps = 0
        d = {"r": (0, 1), "l": (0, -1), "u": (-1, 0), "d": (1, 0)}
        curr_d = d['r']
        k, l = 0, 0
        while head and (k < m and l < n):
            # curr = head.val
            # Print the first row from
            # the remaining rows
            for i in range(l, n):
                matrix[k][i] = head.val
                if head.next:
                    head = head.next
                else:
                    return matrix

            k += 1

            # Print the last column from
            # the remaining columns
            for i in range(k, m):
                matrix[i][n - 1] = head.val
                if head.next:
                    head = head.next
                else:
                    return matrix

            n -= 1

            # Print the last row from
            # the remaining rows
            if (k < m):

                for i in range(n - 1, (l - 1), -1):
                    matrix[m - 1][i] = head.val
                    if head.next:
                        head = head.next
                    else:
                        return matrix

                m -= 1

            # Print the first column from
            # the remaining columns
            if (l < n):
                for i in range(m - 1, k - 1, -1):
                    matrix[i][l] = head.val
                    if head.next:
                        head = head.next
                    else:
                        return matrix

                l += 1
            # head = head.next
        return matrix