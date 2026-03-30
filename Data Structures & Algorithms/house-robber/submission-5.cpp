class Solution {
public:
    int rob(vector<int>& nums) {
        int one = 0;
        int two = 0;

        for (int i = 0; i < nums.size(); i++) {
            int tmp = max(one + nums[i], two);
            one = two;
            two = tmp;
        }

        return two;
    }
};
