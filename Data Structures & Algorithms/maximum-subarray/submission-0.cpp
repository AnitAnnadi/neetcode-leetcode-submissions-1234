class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = 0;
        int maxSum = nums[0];

        for (int num : nums) {
            if (currSum < 0) {
                currSum = 0;
            }

            currSum += num;

            if (currSum > maxSum) {
                maxSum = currSum;
            }
        }

        return maxSum;
    }
};
