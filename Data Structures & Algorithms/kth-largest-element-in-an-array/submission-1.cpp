class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> maxPq(nums.begin(), nums.end());

        for (int i = 0; i < k - 1; i++) {
            maxPq.pop();
        }

        return maxPq.top();
    }
};
