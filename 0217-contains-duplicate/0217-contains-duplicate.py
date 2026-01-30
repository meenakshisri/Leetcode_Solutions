class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        """
        numset = set(nums)

        if len(numset) != len(nums):
            return True
        return False
        """

        numset = set()

        for i in range(len(nums)):
            if nums[i] in numset:
                return True
            numset.add(nums[i])
            
        return False
            



