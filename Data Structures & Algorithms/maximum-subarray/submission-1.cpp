class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int currSum = 0;
        int maxSum = nums[0];

        for (int num : nums) {
            currSum = max(num, currSum + num);

            if (currSum > maxSum) {
                maxSum = currSum;
            }
        }

        return maxSum;
    }
};
