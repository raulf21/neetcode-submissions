class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create the dictionary to hold our groups
        anagrams = defaultdict(list)

        for s in strs:
            # Create the scoreboard for all 26 characters in the alphabet
            count = [0] * 26

            for char in s:
                # ord('a') is 97. 
                index = ord(char) - ord('a')
                count[index] +=1

            key = tuple(count)

            anagrams[key].append(s)

        return list(anagrams.values())

        

        