# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1 -> 2 -> 3 -> 4

# 1 -> 2 -> 4

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head

        while cur:
            cur = cur.next
            i += 1
        
        i -= n

        # _ -> 1 -> 2

        tail = ans = ListNode()
        tail.next = head
        for j in range(i):
            tail = tail.next
        
        tail.next = tail.next.next
        return ans.next
        
