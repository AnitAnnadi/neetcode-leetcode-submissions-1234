class Solution {
public:
    int climbStairs(int n) {

        if (n < 2) {
            return 1;
        }

        int step1 = 1;
        int step2 = 2;

        int i = 3;
        while (i <= n) {
            int tmp = step2;
            step2 = step1 + step2;
            step1 = tmp;
            i++;
        }

        return step2;
    }
};
