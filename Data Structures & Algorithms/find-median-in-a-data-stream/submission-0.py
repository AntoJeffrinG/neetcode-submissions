import heapq
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        #check for the ordering
        if self.small and self.large and -self.small[0] > self.large[0]:
            element = heapq.heappop(self.small)
            heapq.heappush(self.large,-element)

        #check for size
        if len(self.small) > len(self.large) + 1:
            element = -heapq.heappop(self.small)
            heapq.heappush(self.large,element)

        if len(self.large) > len(self.small) + 1:
            element = heapq.heappop(self.large)
            heapq.heappush(self.small,-element)
        

    def findMedian(self) -> float:
        if (len(self.small) + len(self.large)) % 2 == 0:
            return (-self.small[0] + self.large[0]) / 2
        if len(self.small) > len(self.large):
            return -self.small[0]

        return self.large[0]
        
        