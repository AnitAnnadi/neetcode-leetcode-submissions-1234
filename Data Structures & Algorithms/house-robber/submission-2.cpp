class Solution {
public:
    int rob(vector<int>& nums) {

        if (nums.size() < 2) return nums[0];

        int sum1 = nums[0];
        int sum2 = nums[1];

        int i = 2;
        while (i < nums.size()) {
            if (i + 1 < nums.size() && sum2 > sum1) {
                sum2 += nums[i + 1];
            } else if (i + 1 < nums.size()) {
                sum2 = sum1 + nums[i + 1];
            }

            sum1 += nums[i];
            i += 2;
        }

        return max(sum1, sum2);
    }
};
