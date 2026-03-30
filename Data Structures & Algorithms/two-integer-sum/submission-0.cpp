class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> m;
        vector<int> res;

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (m.count(diff)) {
                res.push_back(m[diff]);
                res.push_back(i);
                return res;
            }

            m[nums[i]] = i;
        }
    }
};
