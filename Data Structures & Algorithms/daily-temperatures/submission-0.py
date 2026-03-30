class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        n = len(temperatures)
        res = []

        for i in range(n - 1, -1, -1):
            temp = temperatures[i]
            while s and s[-1][0] < temp:
                s.pop()

            if s:
                res.append(s[-1][1] - i)
            else:
                res.append(0)
            
            s.append((temp, i))
        
        res.reverse()
        return res