class Solution {
public:
    int climbStairs(int n) {
        int distinctSteps = 1;
        

        for (int i = 0; i < n; i++) {
            if (i + 2 <= n) {
                distinctSteps++;
            }
        }

        return distinctSteps;
    }
};
