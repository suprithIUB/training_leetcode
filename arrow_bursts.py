class Solution:
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        if not points:
            return 0
        
        from operator import itemgetter
        points.sort(key=itemgetter(0))
        
        import heapq
        min_heap = []
        
        
        arrows = 0
        for i in range(0, len(points)):
            if not min_heap:
                heapq.heappush(min_heap, points[i][1])
            elif points[i][0] > min_heap[0]:
                arrows += 1
                min_heap = []
                min_heap.append(points[i][1])
            else:
                heapq.heappush(min_heap, points[i][1])
        
        if min_heap:
            arrows += 1
        return arrows
    

