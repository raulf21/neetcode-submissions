class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        # Create a frequency array for heights up to 100
        counts = [0] * 101

        for h in heights:
            counts[h] +=1
        
        mismatches = 0
        current_height = 0

        # Iterate through original heights
        for actual_heights in heights:
            # Find the next expected hieght taht actuall exists in our counts
            while counts[current_height] == 0:
                current_height +=1

            # if the actual_height doesn't match the expect height, its a mismatch
            if actual_heights != current_height:
                mismatches +=1

            # "Place" the students by decrementing thier count
            counts[current_height] -=1
        return mismatches
        