# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # 678 + 398
        # 1873465786345876348756287645287346587236458723645 + 6378465782365498273598723857298457983475982475

        # 8
        # 10

        # 8
        # 0 1

        # 8 1

        # 18

        # 521 + 654

        # 5 2 1
        # 3 9 4

        # 8 1 6

        # 618

        carry = 0

        tail = ans = ListNode(-1)

        while (l1 or l2 or carry):
            sumi = carry
            if l1:
                sumi += l1.val
            if l2:
                sumi += l2.val
            cur = ListNode((sumi) % 10)
            carry = int(sumi >= 10)

            tail.next = cur
            tail = tail.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next




