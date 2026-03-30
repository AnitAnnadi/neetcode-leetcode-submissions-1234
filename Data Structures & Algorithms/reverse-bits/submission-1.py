class Solution:
    def reverseBits(self, n: int) -> int:
        r = 0

        for i in range(32):
            r = r << 1        
            if n & 1:
                r = r | 1
            
            n = n >> 1

        return r