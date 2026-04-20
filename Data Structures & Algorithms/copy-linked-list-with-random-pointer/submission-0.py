"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        hashmap = {}

        oldNode = head
        while oldNode:
            hashmap[oldNode] = Node(oldNode.val)
            oldNode = oldNode.next
        
        oldTemp = head
        while oldTemp:
            newnode = hashmap[oldTemp]
            if oldTemp.next:
                nexttoConnect = hashmap[oldTemp.next]
                newnode.next = nexttoConnect
            if oldTemp.random:
                randomtoConnect = hashmap[oldTemp.random]
                newnode.random = randomtoConnect
            oldTemp = oldTemp.next
        
        return hashmap[head]

        

        

        