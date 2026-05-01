class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket1Fruit, basket1Count = -1, 0
        basket2Fruit, basket2Count = -1, 0
        l, maxFruits = 0, 0

        for r in range(len(fruits)):
            fruit = fruits[r]
            if basket1Count == 0:
                basket1Fruit = fruit
            elif basket2Count == 0:
                basket2Fruit = fruit

            if fruit == basket1Fruit:
                basket1Count += 1
            elif fruit == basket2Fruit:
                basket2Count += 1
            else:
                while l < r and basket1Count and basket2Count:
                    fruit_l = fruits[l]
                    if fruit_l == basket1Fruit:
                        basket1Count -= 1 
                    elif fruit_l == basket2Fruit:
                        basket2Count -= 1
                    
                    l += 1

                if basket1Count == 0:
                    basket1Fruit, basket1Count = fruit, 1
                else:
                    basket2Fruit, basket2Count = fruit, 1

            maxFruits = max(maxFruits, basket1Count + basket2Count)

        return maxFruits

