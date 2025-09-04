class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_hashMap = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            
            if complement in my_hashMap:
                return i, my_hashMap.get(complement)

            my_hashMap[nums[i]] = i