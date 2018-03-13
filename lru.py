class Node:
    def __init__(self, item=None, key=None,nex=None, prev=None):
        self.item = item
        self.key = key
        self.nex = nex
        self.prev = prev

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __sizeof__(self):
        return self.size

    def prepend(self, item, key):
        node = Node(item, key)
        # first node
        node.nex = self.head
        if not self.head:
            self.tail = node
        else:
            self.head.prev = node
        self.head = node
        self.size += 1

        return node

    def moveFront(self, node):
        # only one node or first node, return
        if self.head == self.tail or self.head == node:
            return
        else:
            if self.tail == node:
                self.tail = self.tail.prev
                self.tail.nex.prev = None
                self.tail.nex = None
            if node.prev:
                node.prev.nex = node.nex
                node.nex.prev = node.prev
            node.nex = self.head
            self.head.prev = node
            node.prev = None
            self.head = node
                
    def __str__(self):
        if self.head == self.tail == None:
            return
        tempNode = self.head

        li = []
        while tempNode:
            #print(tempNode.item)
            li.append(tempNode.item)
            tempNode = tempNode.nex
        return "  ".join(str(e) for e in li).strip()

    def removeTailNode(self):
        # empty
        if self.head == self.tail == None:
            return
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.nex.prev = None
            self.tail.nex = None
            
class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache_list = LinkedList()
        self.cache_map = dict()
        self.current_size = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache_map:
            val = self.cache_map[key].item
            self.cache_list.moveFront(self.cache_map[key])
            return val
        else:
            return -1

        
    def evict(self):
        remove_key = self.cache_list.tail.key
        self.cache_list.removeTailNode()
        self.cache_map.pop(remove_key)
        self.current_size -= 1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache_map:
            self.cache_list.moveFront(self.cache_map[key])
            self.cache_list.head.item = value
            return
    
        if self.current_size == self.capacity:
            # evict
            self.evict()

        self.current_size += 1
        self.cache_map[key] = self.cache_list.prepend(value, key)


        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
