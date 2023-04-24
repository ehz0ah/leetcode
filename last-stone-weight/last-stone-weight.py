class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # convert stones to negative numbers for max heap
        # python only uses min-heap thus the negative
        max_heap = [-stone for stone in stones]
        # heapq is python built in way to make a heap by using method heapify
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # get the two largest/most negative stones using heappop method
            # heappop in python actually returns the smallest element hence use - sign to get largest
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            # smash the two stones together
            # append/heappush stone1 - stone2 back into max_heap
            # there's also heapreplace where python replaces the smallest element with a value provided when using heapreplace
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        # if there is only one stone left, return its positive value
        if max_heap:
            # remember to undo the -ve sign
            return -max_heap[0]
        else:
            # when there's no more elements in the heap
            return 0
        
        


