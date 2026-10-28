class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        #boyer moore voting algorithm
        candidate = 0
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            else:
                if num == candidate:
                    count = count+1
                else:
                    count = count-1
        return candidate
        