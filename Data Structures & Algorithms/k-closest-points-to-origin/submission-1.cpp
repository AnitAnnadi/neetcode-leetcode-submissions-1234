class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<int, vector<int>>> maxPq;

        for(int i = 0; i < points.size(); i++) {
            int distance = sqrt(pow(abs(points[i][0]), 2) + pow(abs(points[i][1]), 2));
            maxPq.push({distance, points[i]});

            if (maxPq.size() > k) {
                maxPq.pop();
            }
        }

        vector<vector<int>> answers;
        while(!maxPq.empty()) {
            answers.push_back(maxPq.top().second);
            maxPq.pop();
        }

        return answers;
    }
};
