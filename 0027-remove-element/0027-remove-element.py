class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insertPos = 0

        for i in range(len(nums)) :

                if nums[i] != val :
                    nums[insertPos] = nums[i]
                    insertPos += 1

        return insertPos