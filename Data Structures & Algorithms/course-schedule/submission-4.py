class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for a, b in prerequisites:
            preMap[a].append(b)
        

        visted = set()

        def dfs(crs):
            if crs in visted:
                return False
            if preMap[crs] == []:
                return True

            visted.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visted.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True


        