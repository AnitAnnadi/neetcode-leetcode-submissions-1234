class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            while s and s[-1][0] <= temp:
                s.pop()

            if s:
                res[i] = s[-1][1] - i
            
            s.append((temp, i))
        
        return res