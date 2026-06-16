import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Build adjacnency list
        adj = {i: [] for i in range(n)}
        for u,v, w in edges:
            adj[u].append((v,w))
        
        # Initalize distances
        distances = {}
        for i in range(n):
            if i == src:
                distances[i] = 0
            else:
                distances[i] = float('inf')
        minHeap = [(0, src)] # (distance = 0, vertex = src)

        while minHeap:
            currDistance, vertex = heapq.heappop(minHeap)

            # Skip wif we already found a better path
            if currDistance > distances[vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in adj[vertex]:
                newDistance = currDistance + weight

                if newDistance < distances[neighbor]:
                    distances[neighbor] = newDistance
                    heapq.heappush(minHeap, (newDistance, neighbor))

        for vertex in distances:
            if distances[vertex] == float('inf'):
                distances[vertex] = -1
        return distances


