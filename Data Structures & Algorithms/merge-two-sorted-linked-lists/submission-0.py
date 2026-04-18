# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        solutionNode = dummyNode

        while list1 and list2:
            if list1.val < list2.val:
                solutionNode.next = list1
                next_node_of_list1 = list1.next
                list1 = next_node_of_list1
            else:
                solutionNode.next = list2
                next_node_of_list2 = list2.next
                list2 = next_node_of_list2
            
            next_node_of_solution = solutionNode.next
            solutionNode = next_node_of_solution
        if list1:
            solutionNode.next = list1
        elif list2:
            solutionNode.next = list2
        return dummyNode.next
        