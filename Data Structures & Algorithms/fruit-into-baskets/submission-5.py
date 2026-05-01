class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts = defaultdict(int)
        l, total, res = 0, 0, 0 

        for r in range(len(fruits)):
            fruit_r = fruits[r]
            counts[fruit_r] += 1
            total += 1

            while len(counts) > 2:
                fruit_l = fruits[l]
                counts[fruit_l] -= 1
                total -= 1

                if counts[fruit_l] == 0:
                    counts.pop(fruit_l)

                l += 1

            res = max(res, total)

        return res

