class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        people.sort()

        numLeft = len(people)
        boats = 0

        while l < r:
            while l < r and people[l] + people[r] > limit:
                r -= 1
            
            if l < r:
                numLeft -= 2
                boats += 1
                r -= 1
                l += 1
        
        return boats + numLeft
