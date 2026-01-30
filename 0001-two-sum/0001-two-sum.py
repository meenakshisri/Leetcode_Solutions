class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numsDict = {}  #Using dictionary to store record for Key, Value pair

        for i, val in enumerate(nums):
            comp = target - val

            if comp in numsDict :
                return [i, numsDict[comp]]
            numsDict[val] = i

        return []

        