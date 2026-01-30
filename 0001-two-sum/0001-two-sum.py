class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}

        for i, val in enumerate(nums):
            comp = target - val

            if comp in numsDict :
                return [i, numsDict[comp]]
            numsDict[val] = i

        return []

        