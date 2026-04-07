class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        num_Set = set()

        for num in nums:
            if num in num_Set:
                return True
            num_Set.add(num)

        return False
        