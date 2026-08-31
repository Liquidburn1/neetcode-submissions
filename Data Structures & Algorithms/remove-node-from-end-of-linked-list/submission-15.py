# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tempnode=ListNode(0,head)
        left=tempnode
        right=head
        while n>0 and right:
            right=right.next
            n-=1
        
        while left and right:
            right=right.next
            left=left.next
        left.next=left.next.next
        return tempnode.next

        #0->5->r
        
