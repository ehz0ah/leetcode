# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        placeholder = []
        dum = dummy = ListNode()
        while head:
            if head.val not in placeholder:
                placeholder.append(head.val)
                dum.next = head
                head, dum = head.next, head
            
            else:
                if head.val in placeholder and head.next == None:
                    dum.next = None
                    break
                head = head.next
        return dummy.next
