class Solution {    
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> maxPq(stones.begin(), stones.end());

        while (maxPq.size() > 1) {
            int x = maxPq.top();
            maxPq.pop();
            int y = maxPq.top();
            maxPq.pop();

            if (x != y) {
                maxPq.push(x - y);
            }
        }

        if (maxPq.empty()) {
            return 0;
        }

        return maxPq.top();
    }
};
