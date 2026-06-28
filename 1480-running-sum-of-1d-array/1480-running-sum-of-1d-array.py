class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        n = len(nums)
        sum = 0
        res = []

        for i in range(n):
            sum += nums[i]
            res.append(sum)
        
        return res
        