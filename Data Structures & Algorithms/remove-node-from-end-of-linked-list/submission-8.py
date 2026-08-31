# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        size=0
        while temp:
            size+=1
            temp=temp.next
        index=size-n
        
       
        
        if index==0:
            return head.next
        
        print(size,index)
        i=1
        temp=head
        while i!=index:
            print(i)
            i+=1
            temp=temp.next

        temp.next=temp.next.next

        return head


        