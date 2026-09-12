import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num,0) + 1
        
        heap = []
        for number, frequency in freq.items():
            heapq.heappush(heap,(frequency,number))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [num for fre,num in heap]
        