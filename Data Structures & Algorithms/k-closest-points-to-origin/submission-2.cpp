class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<pair<double, vector<int>>> maxPq;

        for(int i = 0; i < points.size(); i++) {
            double distance = sqrt(points[i][0] * points[i][0] + points[i][1] * points[i][1]);
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
