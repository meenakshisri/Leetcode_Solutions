class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
       
        l, r = 0, len(people)-1
        count = 0
        people.sort()

        while l<=r :
            totalWeight = people[l]+people[r]
            if totalWeight == limit:
                count +=1
                l +=1
                r -=1
            elif totalWeight > limit:
                count +=1
                r -=1
            else:
                count += 1
                l += 1
                r -= 1
        return count


