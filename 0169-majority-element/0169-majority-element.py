class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #boyer moore voting algorithm
        candidate = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if count == 0:
                candidate = nums[i]
                count = 1
            else:
                if nums[i] == candidate:
                    count = count+1
                else:
                    count = count-1
        return candidate
        