class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        int currSum = nums[0];
        int maxSum = nums[0];

        int maxL = 0;
        int maxR = 0;

        int L = 0;
        int R = 1;

        while (maxL != R % nums.size()) {
            if (currSum < 0) {
                currSum = 0;
                L = R;
            }

            currSum += nums[R % nums.size()];
            if (currSum > maxSum) {
                maxSum = currSum;
                maxL = L % nums.size();
                maxR = R % nums.size();
            }
            
            R++;
        }

        return maxSum;
    }
};