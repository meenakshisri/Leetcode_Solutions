class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i, j = 1, 2

        while(j<len(nums)):
            if nums[i-1] != nums[j]:
                i += 1
                nums[i] = nums[j]            
            j +=1
        return i+1
        