class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        if n<=2:
            return n

        i, j = 1, 2

        for j in range(2, n):
            if nums[i-1] != nums[j]:
                i += 1
                nums[i] = nums[j]            
            j +=1
        return i+1
        