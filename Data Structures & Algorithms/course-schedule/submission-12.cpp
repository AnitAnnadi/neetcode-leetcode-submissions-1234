class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_set<int> coursesTaken;
        unordered_map<int, vector<int>> adj;

        for (int i = 0; i < numCourses; i++) {
            adj[i] = {};
        } 

        for (vector<int> pair : prerequisites) {
            adj[pair[1]].push_back(pair[0]);
        }

        while (coursesTaken.size() < numCourses) {
            int coursesTakenInCycle = 0;

            for (auto it = adj.begin(); it != adj.end();) {
                int canTakeCourse = true;
                for (int course : it->second) {
                    if (!coursesTaken.count(course)) {
                        canTakeCourse = false;
                    }
                }

                if (canTakeCourse) {
                    coursesTaken.insert(it->first);
                    it = adj.erase(it);
                    coursesTakenInCycle++;
                } else {
                    it++;
                }
            }

            if (coursesTakenInCycle == 0) {
                return false;
            }
         }

         return true;
    }
};
