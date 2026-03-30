class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []
        for i in range(n + 1):
            currNum = i
            count = 0
            for i in range(32):
                if currNum & 1 == 1:
                    count += 1
                
                currNum = currNum >> 1
            
            counts.append(count)
        
        return counts