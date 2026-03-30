class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        for (auto i = nums.end() -  1; i != nums.begin(); i--) {
            if (*i == *(i-1)) {
                nums.erase(i);
            }
        }

        return nums.size();
    }
};