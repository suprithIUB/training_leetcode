class BSTInterval:
    def __init__(self):
        self.root = None

    def add(self, start, end):
        new_node = BSTNode(start, end, end)
        if not self.root:
            self.root = new_node
        else:
            stack = []
            current_node = self.root

            while current_node:
                parent = current_node
                stack.append(parent)
                if start < current_node.start:
                    current_node = current_node.left
                else:
                    current_node = current_node.right

            if start < parent.start:
                parent.left = new_node
            else:
                parent.right = new_node

            #update end points along the path
            while stack:
                if stack[-1].max_end_point < end:
                    stack[-1].max_end_point = end
                stack.pop()


    def check_intersection(self, start, end, node):
        if not node:
            return False
        print("start %s end %s node.start %s node.end %s"%(start, end, node.start, node.end))
        if (start <= node.start and end >= node.end) or (node.start <= start and start < node.end) or (node.start < end and end <= node.end):
            return True
        return False
        
    def search_interval(self, start, end):
        if not self.root:
            return False
        current_node = self.root
        while current_node:
            if self.check_intersection(start, end, current_node):
                return True
            elif not current_node.left:
                current_node = current_node.right
            elif current_node.left.max_end_point <= start:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False

class BSTNode:
    def __init__(self, start, end, max_end_point):
        self.start = start
        self.end = end
        self.max_end_point = max_end_point
        self.left = None
        self.right = None

class MyCalendar:
    def __init__(self):
        self.tree = BSTInterval() 

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        intersection = self.tree.search_interval(start, end)
        if intersection:
            return False
        else:
            self.tree.add(start, end)
            return True

if __name__ == "__main__":
    '''
    so_cal = MyCalendar()
    bookings = [[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]
    for item in bookings:
        print(so_cal.book(item[0], item[1]))
    '''
    bookings =[[97,100],[33,51],[89,100],[83,100],[75,92],[76,95],[19,30],[53,63],[8,23],[18,37],[87,100],[83,100],[54,67],[35,48],[58,75],[70,89],[13,32],[44,63],[51,62],[2,15]]
    
    new_cal = MyCalendar()
    for item in bookings:
        print(new_cal.book(item[0], item[1]))
