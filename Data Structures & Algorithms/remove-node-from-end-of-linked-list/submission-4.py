# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)

        # First loop
        length = 0
        curr = head
        while curr is not None:
            length += 1
            curr = curr.next


        stepToTarget = length - n

        # Second loop
        curr = dummy
        for _ in range(stepToTarget):
            curr = curr.next

        curr.next = curr.next.next

        return dummy.next


        
