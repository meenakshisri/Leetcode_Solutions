class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        result = []
        nums.sort()

        for i, n in enumerate(nums):
            if (i>0) and (n == nums[i - 1]) :
                continue
            
            l, r = i+1, len(nums)-1
            while l<r:
                if (n + nums[l] + nums[r] > 0):
                    r = r-1
                elif (n + nums[l] + nums[r] <0):
                    l= l+1
                else:
                    result.append([n, nums[l], nums[r]])
                    l = l+1
                    while nums[l] == nums[l-1] and l<r :
                        l = l+1
        
        return result







        