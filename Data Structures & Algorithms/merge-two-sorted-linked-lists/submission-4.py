# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=list1
        cur2=list2
        newlist=ListNode()
        newcur=newlist
        while cur1 and cur2:
            if cur1.val>cur2.val:
                newcur.next=cur2
                cur2=cur2.next
            elif cur1.val<=cur2.val:
                newcur.next=cur1
                cur1=cur1.next
            newcur=newcur.next
        
        if cur1:
            newcur.next=cur1
        else:
            newcur.next=cur2
        return newlist.next