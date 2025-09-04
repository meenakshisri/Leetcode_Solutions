class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        count = {}
        majElement, maxCount = 0, 0
        
        for n in nums :
            count[n] = count.get(n, 0) + 1
            if count[n] > maxCount :
                majElement = n
                maxCount = max(count[n], maxCount)
        
        return majElement
    """

    #Using Boyer Moore Majority Voting Algorithm

        majElement = 0
        count = 0

        for n in nums :
            if count == 0 :
                majElement = n
            count += (1 if n == majElement else -1)
        
        return majElement


