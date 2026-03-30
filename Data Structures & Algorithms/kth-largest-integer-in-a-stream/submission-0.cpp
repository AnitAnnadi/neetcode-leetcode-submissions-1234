class KthLargest {
private:
    int k;
    priority_queue<int> maxPq;
public:
    KthLargest(int k, vector<int>& nums) {
        this->k = k;

        for (int i = 0; i < nums.size(); i++) {
            maxPq.push(nums[i]);
        }
    }
    
    int add(int val) {
        maxPq.push(val);
        priority_queue copyMaxPq = maxPq;

        for(int i = 1; i < k; i++) {
            copyMaxPq.pop();
        }

        return copyMaxPq.top();
    }
};
