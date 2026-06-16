class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = [[]]

        for num in nums:
            newPerm = []
            for p in perms:
                for j in range(len(p)+1):
                    copyP = p.copy()
                    copyP.insert(j, num)
                    newPerm.append(copyP)

            perms = newPerm
        return perms



        