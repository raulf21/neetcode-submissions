class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        while i>=0 or j>= 0 or carry:
            val_a = int(a[i]) if i>=0 else 0
            val_b = int(b[j]) if j>=0 else 0

            cur_sum = val_a + val_b + carry
            carry = cur_sum // 2
            digit = cur_sum % 2
            result.append(str(digit))

            i -=1
            j-=1
        return "".join(reversed(result))
        

            

        