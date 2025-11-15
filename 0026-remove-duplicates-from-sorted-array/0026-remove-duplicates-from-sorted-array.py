class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 0 #To keep track of current unique element

        for j in range(1, len(nums)): #to parse through complete array
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i+1 # returning number of unique elements
        