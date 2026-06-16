class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}

        for s in strs:
            wordSorted = ''.join(sorted(s))
            if wordSorted in group:
                group[wordSorted].append(s)
            else:
                group[wordSorted] = [s]
        return group.values()
        