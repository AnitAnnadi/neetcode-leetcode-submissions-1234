class KthLargest {
private:
    int k;
    priority_queue<int, vector<int>, greater<int>> minPq;
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;

        for (int i = 0; i < nums.size(); i++) {
            minPq.push(nums[i]);

            if (minPq.size() > k) {
                minPq.pop();
            }
        }
    }
    
    int add(int val) {
        minPq.push(val);

        if (minPq.size() > k) {
            minPq.pop();
        }

        return minPq.top();
    }
};
