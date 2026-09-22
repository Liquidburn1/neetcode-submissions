# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head==None:
            return 
        cur=head.next
        prev=head
        prev.next=None
       
        while cur:
            temp=cur
            cur=cur.next
            temp.next=prev
            prev=temp
            
        
        
        return prev


