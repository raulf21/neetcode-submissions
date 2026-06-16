class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.arr = nums
        self.tree = [0] * (4 * self.n)
        self.build(0,0,self.n-1)

    def build(self, node, start, end):
        # Base case: leaf node
        if start == end:
            self.tree[node] = self.arr[start]
            return 

        # recusive case: internal node
        mid = (start + end) // 2
        left_child = 2 * node + 1 
        right_child = 2 * node + 2

        self.build(left_child, start, mid)
        self.build(right_child, mid + 1, end)
        
        self.tree[node] = self.tree[left_child] + self.tree[right_child]

    def _update_helper(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return 

        mid = (start + end) // 2
        left = (2 * node + 1)
        right = (2 * node + 2)

        if idx <= mid:
            self._update_helper(left, start, mid, idx, val)
        else:
            self._update_helper(right, mid+1, end, idx, val)

        self.tree[node] = self.tree[left] + self.tree[right]
    
    def update(self, index: int, val: int) -> None:
        self._update_helper(0, 0, self.n-1, index, val) 

    def _query_helper(self, node, start, end, L, R):
        # No overlap
        if R < start or end < L:
            return 0

        # Complete overlap-use whole node
        if L <= start and end <= R:
            return self.tree[node]

        # partial coverage - recure its children
        mid = (start + end) // 2
        left = 2 * node + 1
        right = 2 * node + 2

        left_sum = self._query_helper(left, start, mid, L, R)
        right_sum = self._query_helper(right, mid + 1, end, L, R)

        return left_sum + right_sum

    def query(self, L: int, R: int) -> int:
        return self._query_helper(0,0,self.n-1, L, R)

