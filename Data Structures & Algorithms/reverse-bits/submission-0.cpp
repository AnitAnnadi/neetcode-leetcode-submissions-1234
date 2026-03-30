class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int rNum = 0;
        for (int i = 0; i < 32; i++) {
            rNum = rNum << 1;
            if (n % 2 == 1) {
                rNum += 1;
            }

            n = n >> 1;
        }

        return rNum;
    }
};
