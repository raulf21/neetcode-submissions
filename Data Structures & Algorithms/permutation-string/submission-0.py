class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)
    
        if len_s1 > len_s2:
            return False
        
        # Frequency count of s1
        s1_count = Counter(s1)
        # Frequency count of the first window in s2
        s2_count = Counter(s2[:len_s1])
        
        # Check the first window
        if s1_count == s2_count:
            return True
        
        # Start sliding the window
        for i in range(len_s1, len_s2):
            start_char = s2[i - len_s1]
            end_char = s2[i]
            
            # Remove the count of the old character in the window
            s2_count[start_char] -= 1
            if s2_count[start_char] == 0:
                del s2_count[start_char]
            
            # Add the count of the new character in the window
            s2_count[end_char] += 1
            
            # Compare current window count with s1 count
            if s1_count == s2_count:
                return True
        
        return False