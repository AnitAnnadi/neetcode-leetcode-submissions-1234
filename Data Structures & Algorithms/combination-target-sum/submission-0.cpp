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

        if (currSum > target) return;
        
        for (int i = index; i < nums.size(); i++) {
            subset.push_back(nums[i]);
            dfs(res, nums, subset, i, target, currSum + nums[i]);
            subset.pop_back();
        }
    }
};
