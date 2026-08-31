# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res=ListNode()
        cur=res
        carry=0
        num1=0
        num2=0
        while l1 or l2:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            
            
            sum=num1+num2+carry
            if sum>=10:
                carry=1
                sum=sum-10
                cur.next=ListNode(sum,None)
            else:
                carry=0
                cur.next=ListNode(sum,None)
            cur=cur.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
        
        if carry==1:
            cur.next=ListNode(1,None)

        return res.next






        