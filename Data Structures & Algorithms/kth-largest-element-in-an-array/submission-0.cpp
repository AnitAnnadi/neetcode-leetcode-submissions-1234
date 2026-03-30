class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<int>> minPq;

        for (int i = 0; i < nums.size(); i++) {
            minPq.push(nums[i]);

            if (minPq.size() > k) {
                minPq.pop();
            }
        } 

        return minPq.top();
    }
};
