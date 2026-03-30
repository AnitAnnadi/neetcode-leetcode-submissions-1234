class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_set<int> coursesTaken;
        unordered_map<int, vector<int>> adj;

        for (vector<int> pair : prerequisites) {
            if (!adj.count(pair[0])) {
                adj[pair[0]] = {};
            }

            if (!adj.count(pair[1])) {
                adj[pair[1]] = {};
            }

            adj[pair[1]].push_back(pair[0]);
        }

        while (coursesTaken.size() < numCourses) {
            int coursesTakenInCycle = 0;

            for (const auto& pair : adj) {
                if (coursesTaken.count(pair.first)) {
                    continue;
                }

                int canTakeCourse = true;
                for (int course : pair.second) {
                    if (!coursesTaken.count(course)) {
                        canTakeCourse = false;
                    }
                }

                if (canTakeCourse) {
                    coursesTaken.insert(pair.first);
                    coursesTakenInCycle++;
                }
            }

            if (coursesTakenInCycle == 0) {
                return false;
            }
         }

         return true;
    }
};
