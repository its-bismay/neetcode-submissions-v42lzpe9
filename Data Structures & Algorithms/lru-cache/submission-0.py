class ListNode:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.nxt = None
        self.prv = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.left = ListNode(0,0) # least recently used 
        self.right = ListNode(0,0) # most recently used

        self.left.nxt = self.right # left --> right
        self.right.prv = self.left # left <-- right

    # when adding we add the node in right side cause it should be most recently used node
    def add_node(self, node):
        prv_node = self.right.prv

        node.prv = prv_node
        prv_node.nxt = node

        node.nxt = self.right
        self.right.prv = node

    # when removing a node we need to join it's previous node to it's next node   
    def remove_node(self, node):
        prv_node = node.prv
        nxt_node = node.nxt

        prv_node.nxt = nxt_node
        node.prv = prv_node

        nxt_node.prv = prv_node
        node.nxt = nxt_node

    def get(self, key: int) -> int:
        if key in self.cache:
            # if we perform anything on a node it become the most recently used node so we need to shift it to the right part
            self.remove_node(self.cache[key]) # remove node from its current position
            self.add_node(self.cache[key]) # again adding that node to right most part
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # remove the old one
            self.remove_node(self.cache[key])
        
        # make new node with the ket and value and add that to the right most
        self.cache[key] = ListNode(key, value) # create new node
        self.add_node(self.cache[key]) # add that to the linked-list

        if len(self.cache) > self.capacity:
            # remove from the least recently used node
            lru = self.left.nxt
            self.remove_node(lru)
            del self.cache[lru.key] # also remove from the cache
        
