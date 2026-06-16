class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs)-1)


    def mergeSortHelper(self,pairs, start, end):
        if end - start + 1 <= 1:
            return pairs
        
        # find middle index
        m = (start + end) // 2
        # Sort left
        self.mergeSortHelper(pairs, start, m)
        # sort right
        self.mergeSortHelper(pairs, m+1, end)

        # merge both halves
        self.merge(pairs, start, m, end)
        return pairs

    def merge(self, pairs, start, middle, end):
        L = pairs[start:middle+1]
        R = pairs[middle+1: end+1]
        i = 0 # index for L
        j = 0 # index for R
        k = start # index for pairs

        # Merge the two sorted halfs into the original array
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i +=1
            else:
                pairs[k] = R[j]
                j +=1
            k +=1

        # one of the halfs will have elements remaining
        while i < len(L):
            pairs[k] = L[i]
            i +=1
            k +=1
        while j < len(R):
            pairs[k] = R[j]
            j +=1
            k +=1