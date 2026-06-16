class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        targetMap = defaultdict(int)
        for i in range(len(numbers)):
            temp = target - numbers[i]
            if targetMap[temp]:
                return [targetMap[temp], i + 1]
            targetMap[numbers[i]] = i + 1
        return []


        
        