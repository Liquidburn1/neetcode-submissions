# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        rethead=ListNode(0,None)
        retcur=rethead

        while list1 and list2:
            if list1.val<=list2.val:
                retcur.next=list1
                list1=list1.next
                retcur=retcur.next
                retcur.next=None

            else:
                retcur.next=list2
                list2=list2.next
                retcur=retcur.next
                retcur.next=None


        if list1:
            retcur.next=list1

        elif list2:
            retcur.next=list2

        return rethead.next
