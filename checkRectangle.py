import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(p1, p2):
    return math.pow((p1.x - p2.x), 2) + math.pow((p1.y - p2.y), 2)

def checkRectangle(p1, p2, p3, p4):
    d2 = dist(p1, p2)
    d3 = dist(p1, p3)
    d4 = dist(p1, p4)

    if (d2 + d3) == d4:
        d2_ = dist(p4, p2)
        d3_ = dist(p4, p3)
        if min(d2,d3) == min(d2_, d3_) and max(d2,d3) == max(d2_, d3_):
            return True

    if (d3 + d4) == d2:
        d3_ = dist(p2, p3)
        d4_ = dist(p2, p4)
        if min(d3, d4) == min(d3_, d4_) and max(d3, d4) == max(d3_, d4_):
            return True

    if (d4 + d2) == d3:
        d4_ = dist(p3, p4)
        d2_ = dist(p3, p2)
        if min(d4, d2) == min(d4_, d2_) and max(d4, d2) == max(d4_, d2_):
            return True
    return False

if __name__ == "__main__":
    p1 = Point(1,1)

    p2 = Point(4,1)

    p3 = Point(1,5)

    p4 = Point(4,5)
    
    print(checkRectangle(p1, p2, p3, p4))

    p4 = Point(-3,5)

    print(checkRectangle(p1, p2, p3, p4))
    
    """check for square"""
    p2 = Point(5,1)
    p4 = Point(5,5)
    print(checkRectangle(p1, p2, p3, p4))
    
    p1 = Point(20, 10)
    p2 = Point(10, 20)
    p3 = Point(20, 20)
    p4 = Point(10, 10)
    
    print(checkRectangle(p1, p2, p3, p4))
