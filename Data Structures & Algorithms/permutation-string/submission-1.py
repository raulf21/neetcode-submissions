class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1>len2:
            return False
        count1 = Counter(s1)
        count2 = Counter(s2[:len1])

        if count1 == count2:
            return True
        
        for r in range(len1,len2):
            start = s2[r-len1]
            end = s2[r]

            count2[start] -=1
            if count2[start] == 0:
                del count2[start]

            count2[end] +=1
            if count1 == count2:
                return True
        return False
