class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # start from the end and move backwards
        for d in range(len(digits)-1,-1,-1):
            if digits[d] < 9:
                digits[d] +=1
                return digits

            # if it was 9 then we the loop carries 1 to the left
            digits[d] = 0
        return [1] + digits
        