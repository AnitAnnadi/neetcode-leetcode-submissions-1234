class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        pairs = []

        for i in range(n):
            pairs.append((position[i], speed[i]))
        pairs.sort()

        s = []
        for pos, spd in pairs:
            t = (target - pos) / spd

            while s and s[-1] <= t:
                s.pop()

            s.append(t)
            
        return len(s)