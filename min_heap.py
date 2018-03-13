class MinHeap():
    def __init__(self):
        self.array = [-1]

    def add(self, item):
        self.array.append(item)
        if len(self.array) > 2:
            self.bubble_up(len(self.array)-1)

    def heap_size(self):
        return len(self.array)

    def extract_min(self):
        if self.array:
            item = self.array[1]
            self.array[1] = self.array[-1]
            self.array.pop()
            self.bubble_down()
            return item
        else:
            raise NameError("No elements in heap")

    def peek_min(self):
        if self.array:
            return self.array[1]
        else:
            raise NameError("No elements in heap")

    def has_parent(self, child):
        return self.get_parent

    def has_left_child(self, child):
        return self.get_left_child(child)

    def has_right_child(self, child):
        return self.get_right_child(child)

    def get_parent(self, child):
        parent = child//2
        if parent >= 1 and parent < len(self.array):
            return parent
        return 0
    
    def get_left_child(self, parent):
        left  = (parent * 2)
        if left < len(self.array) and left > 1:
            return left
        return 0

    def get_right_child(self, parent):
        right = (parent * 2) + 1
        if right > 1 and right < len(self.array):
            return right
        return 0

    def bubble_down(self):
        parent = 1
        while self.has_left_child(parent):
            smaller_child = self.get_left_child(parent)
            if self.has_right_child(parent):
                right_child = self.get_right_child(parent)
                if self.array[right_child] < self.array[smaller_child]:
                    smaller_child = right_child
            if self.array[parent] < self.array[smaller_child]:
                break

            self.array[parent], self.array[smaller_child] = self.array[smaller_child], self.array[parent]
            parent = smaller_child

    def bubble_up(self, indx):
        while self.has_parent(indx):
            parent = self.get_parent(indx)
            if self.array[parent] < self.array[indx]:
                break
            left_child = self.get_left_child(parent)
            right_child = self.get_right_child(parent)
            smaller_child = right_child if self.array[right_child] < self.array[left_child] else left_child
            # swap
            self.array[parent], self.array[smaller_child] = self.array[smaller_child], self.array[parent]
            indx = parent

    def print_heap(self):
        print(self.array)

if __name__ == "__main__":
    mh = MinHeap()
    mh.add(3)
    mh.add(5)
    mh.print_heap()
    mh.add(2)
    mh.add(10)
    mh.add(11)
    mh.add(13)
    mh.add(0)
    mh.print_heap()
    print(mh.peek_min())
    print(mh.extract_min())
    
    print(mh.extract_min())
    print(mh.extract_min())
    mh.print_heap()
    print(mh.extract_min())
    print(mh.extract_min())
    mh.print_heap()
