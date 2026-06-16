class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        # we use 4n to ensure we have enough space for any n
        self.tree = [0] * (self.n * 4)
        # Start building from root(index 1) covering range(0, n-1)
        self.build(1, 0, self.n - 1, nums)


    def build(self, i , L , R, nums):
        # base case if L == r we are at leaf node
        if L == R:
            self.tree[i] = nums[L]
            return self.tree[i]

        #Recursive step
        mid = L + (R - L) // 2
        self.tree[i] = self.build(2*i, L, mid, nums) + self.build(2*i + 1, mid + 1, R, nums)
        return self.tree[i]

    
    def update(self, index: int, val: int) -> None:
        self._update_helper(1, 0, self.n - 1, index, val)

    def _update_helper(self, i, L, R, idx, val):
        #base case: we found leaf node at target index
        if L == R: 
            self.tree[i] = val
            return 

        mid = L + (R - L) // 2
        # if idx is less than mid
        if idx <= mid:
            self._update_helper(2 * i, L, mid, idx, val)
        else:
            self._update_helper(2 * i + 1, mid + 1, R, idx, val)

        self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]
    
    def query(self, L: int, R: int) -> int:
        return self._query_helper(1, 0, self.n - 1, L, R)

    def _query_helper(self, i, L, R, qL, qR):
        # 1. No Overlap
        if R < qL or L > qR:
            return 0
        
        # 2. Complete Overlap (The Lucky Moment!)
        if qL <= L and R <= qR:
            return self.tree[i]
        
        # 3. Partial Overlap
        mid = L + (R - L) // 2
        # We ask the left child for whatever part of [qL, qR] it has
        left_sum = self._query_helper(2 * i, L, mid, qL, qR)
        # We ask the right child for whatever part of [qL, qR] it has
        right_sum = self._query_helper(2 * i + 1, mid + 1, R, qL, qR)
        
        return left_sum + right_sum