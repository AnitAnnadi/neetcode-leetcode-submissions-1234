class Solution {
public:
    int climbStairs(int n) {
        int distinctSteps = 1;

        if (n % 2 == 0 && n > 2) {
            distinctSteps++;
        }

        for (int i = 0; i < n; i++) {
            if (i + 2 <= n) {
                distinctSteps++;
            }
        }

        return distinctSteps;
    }
};
