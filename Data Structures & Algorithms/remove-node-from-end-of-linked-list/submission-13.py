# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n==0:
            return head.next
        cur=head
        seen={}
        i=1
        while cur:
            seen[i]=cur
            i+=1
            cur=cur.next
        print(i)
        if i==2:
            return None
        i=i-n
        if seen.get(i-1,-1)==-1:
            return seen[i+1]
        
        seen[i-1].next=seen[i].next
        return head


            
            
        