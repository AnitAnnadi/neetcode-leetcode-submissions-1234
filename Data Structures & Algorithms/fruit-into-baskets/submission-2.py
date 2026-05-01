class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0

        baskets = [[-1, 0], [-1, 0]]
        maxFruits = 0

        while r < len(fruits):
            fruit = fruits[r]
            if baskets[0][1] == 0:
                baskets[0] = [fruit, 0]
            elif baskets[1][1] == 0:
                baskets[1] = [fruit, 0]

            if fruit == baskets[0][0]:
                baskets[0][1] += 1
                r += 1
            elif fruit == baskets[1][0]:
                baskets[1][1] += 1
                r += 1
            else:
                while l < r and baskets[0][1] != 0 and baskets[1][1] != 0:
                    fruit = fruits[l]
                    if fruit == baskets[0][0]:
                        baskets[0][1] -= 1 
                    elif fruit == baskets[1][0]:
                        baskets[1][1] -= 1
                    
                    l += 1

            maxFruits = max(maxFruits, baskets[0][1] + baskets[1][1])

        return maxFruits

