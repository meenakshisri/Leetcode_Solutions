class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l = max(weights)
        r = sum(weights)
        res = r

        def canShip(cap):
            ships = 1
            currCap = cap

            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = cap
                currCap = currCap - w
            
            return ships<=days
        


        while l<=r:

            midCap = (l+r)//2
            if canShip(midCap):
                res = min(res, midCap)
                r = midCap - 1
            else:
                l = midCap+1
        return res
        
 
        
         