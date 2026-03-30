class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int r = nums.size() - 1;

        for (int l = nums.size() - 1; l >= 0; l--) {
            if (nums[l] == val) {
                nums[l] = nums[r];
                nums[r] = val;
                r--;
            }
        }

        return r + 1;
    }
};