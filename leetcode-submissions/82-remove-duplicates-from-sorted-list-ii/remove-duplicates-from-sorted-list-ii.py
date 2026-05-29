# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        d.next = head
        prev, curr = d, head

        while curr and curr.next:
            if curr.val == curr.next.val:
                dupp = curr.val
                while curr and curr.val == dupp:
                    curr = curr.next
                prev.next = curr
            else:
                curr = curr.next
                prev = prev.next
        
        return d.next
                
        