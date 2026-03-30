class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto cmp = [](const vector<int>& a, const vector<int>& b) {
            double distanceA = sqrt(pow(a[0], 2) + pow(a[1], 2));
            double distanceB = sqrt(pow(b[0], 2) + pow(b[1], 2));

            return distanceA > distanceB;
        };

        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> minPq(cmp, points);

        vector<vector<int>> answers;
        for (int i = 0; i < k; i++) {
            answers.push_back(minPq.top());
            minPq.pop();
        }

        return answers;
    }
};
