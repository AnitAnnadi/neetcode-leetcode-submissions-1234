class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        dfs(res, nums, {}, 0, target, 0);
        return res;
    }

    void dfs(vector<vector<int>>& res, vector<int>& nums, vector<int> subset, int index, int target, int currSum) {

        if (currSum == target) {
            res.push_back(subset);
            return;
        }

        if (index >= nums.size() || currSum > target) {
            return;
        }

        dfs(res, nums, subset, index + 1, target, currSum);
        subset.push_back(nums[index]);
        dfs(res, nums, subset, index, target, currSum + nums[index]);
    }
};
