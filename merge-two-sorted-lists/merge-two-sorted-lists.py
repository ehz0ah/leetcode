# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Merge 2 singly linked list
        '''
        make a pointer dum and a empty node dummy
        iterate through the two list
        compare the value of the first nodes of the each list
        then set pointer to the node with the lower value
        then reset original empty node to be the node that u previously set your pointer to 
        repeat
        '''
        dum = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                dum.next = list1
                list1 , dum = list1.next, list1
            else:
                dum.next = list2
                list2, dum = list2.next, list2
        if list1 == None or list2 == None:
            dum.next = list1 if list1 else list2 
        return dummy.next

        
