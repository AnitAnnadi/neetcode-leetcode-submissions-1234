class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> numOnes;

        for (int i = 0; i <= n; i++) {
            int count = 0;
            int num = i;
            for (int j = 0; j < 32; j++) {
                if (num % 2 == 1) {
                    count++;
                }

                num = num >> 1;
            }

            numOnes.push_back(count);
        }

        return numOnes;
    }
};
