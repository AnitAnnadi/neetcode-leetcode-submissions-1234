class Solution {
private:
    vector<vector<int>> arrs;
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        dfs(nums, {}, 0);

        return arrs;
    }

    void dfs(vector<int>& nums, vector<int> arr, int index) {
        if (index >= nums.size()) {
            arrs.push_back(arr);
            return;
        }

        dfs(nums, arr, index + 1);
        arr.push_back(nums[index]);
        dfs(nums, arr, index + 1);
    }
};
