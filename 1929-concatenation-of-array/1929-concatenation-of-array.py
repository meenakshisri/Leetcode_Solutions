class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        
        n = len(nums)
        ans = [0] * 2 * n     #important to note

        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]

        return ans
        
        """
        n = len(nums)
        for i in range(n):
            nums.append(nums[i])
        return nums
        """

        
        