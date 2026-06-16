import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = collections.Counter(nums)

        pq = []

        for num, freq in n.items():
            heapq.heappush(pq,(freq,num))
        
            if len(pq) > k:
                heapq.heappop(pq)
        result = []

        print(pq)
        while pq:
            result.append(heapq.heappop(pq)[1])
        return result
        
        