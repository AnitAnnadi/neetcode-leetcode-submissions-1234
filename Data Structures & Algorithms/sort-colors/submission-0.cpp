class Solution {
public:
    void sortColors(vector<int>& nums) {
        vector<int> counts = {0, 0, 0};

        for (int i = 0; i < nums.size(); i++) {
            counts[nums[i]] = counts[nums[i]] + 1;
        }

        int counter = 0;
        for (int i = 0; i < counts.size(); i++) {
            for (int j = 0; j < counts[i]; j++) {
                nums[counter] = i;
                counter++;
            }
        }
    }
};