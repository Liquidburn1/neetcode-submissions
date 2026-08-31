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
        ret=newlist
        while cur1 or cur2:
            if cur1 and cur2:
                if cur1.val>=cur2.val:
                    newlist.next=cur2
                    cur2=cur2.next
                    newlist=newlist.next
                elif cur1.val<cur2.val:
                    newlist.next=cur1
                    cur1=cur1.next
                    newlist=newlist.next




            elif cur1:
                    newlist.next=cur1
                    cur1=cur1.next
                    newlist=newlist.next

            elif cur2:
                    newlist.next=cur2
                    cur2=cur2.next
                    newlist=newlist.next

        return ret.next
            

            

        