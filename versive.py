from collections import deque
class MovingMaxAverageQueue:

    def __init__(self, size):
        """
        Initialize data structure here.
        :type size: int
        """
        self.size = size
        self.window = deque()
        self.max = deque()
        self.window_sum = 0
        

    def enqueue(self, val):
        """
        :type val: int
        """
        
        self.window.append(val)
        self.window_sum += val
        #maintain max values
        while self.max and self.max[-1] < val:
            self.max.pop()
        self.max.append(val)

        #deque elements in FIFO order if queue size exceeds window size
        if len(self.window) > self.size:
            popped = self.window.popleft()
            self.window_sum -= popped
            if self.max and self.max[0] == popped:
                self.max.popleft()

    def get_max(self):
        """
        :rtype: int
        """
        if len(self.window) < self.size:
            return None

        return self.max[0]

    def get_average(self):
        """
        :rtype: float
        """
        if len(self.window) < self.size:
            return None
        return self.window_sum/len(self.window)

class MovingMaxAverage:

    def __init__(self, iterator, size1, size2):
        """
        Initialize data structure here. Two queues of type MovingMaxAverageQueue for two windows
        :type size: iterator
        """
        self.FIRST_WINDOW = size1
        self.SECOND_WINDOW = size2
        self.first_window = MovingMaxAverageQueue(self.FIRST_WINDOW)
        self.second_window = MovingMaxAverageQueue(self.SECOND_WINDOW)
        self.iterator = iterator

    def enqueue(self, val):
        """
        :type: int
        """
        self.first_window.enqueue(val)
        self.second_window.enqueue(val)

    def get_max_average(self):
        """
        :rtype: tuple
        """
        for val in self.iterator:
            self.enqueue(val)
            yield (self.first_window.get_average(), self.first_window.get_max(), self.second_window.get_average(), self.second_window.get_max())

        return

if __name__ == "__main__":
    it = iter([1, 2, 3, 4, 5, 6])
    #example test cases
    m = MovingMaxAverage(it, 3, 5)
    for tup in m.get_max_average():
        print(tup)
   
    print("---------")
    it = iter([1,3,-1,-3,5,3,6,7])
    #example test cases
    m = MovingMaxAverage(it, 3, 5)
    for tup in m.get_max_average():
        print(tup)

    print("---------")
    #versive ask:
    """
    m = MovingAverage("provide iterator here", 3, 20)
    for tup in m.get_max_average():
        print(tup)

    """
