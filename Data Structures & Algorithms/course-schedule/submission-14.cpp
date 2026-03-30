class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> adj;
        unordered_set<int> coursesTaken;

        for (int i = 0; i < numCourses; i++) {
            adj[i] = {};
        }

        for (vector<int> prereq : prerequisites) {
            adj[prereq[1]].push_back(prereq[0]);
        }   

        for (int i = 0; i < numCourses; i++) {
            unordered_set<int> visited;
            bool canTake = dfs(i, adj, coursesTaken, visited);

            if (!canTake) {
                return false;
            }
        }

        return true;
    }

    bool dfs(int course, unordered_map<int, vector<int>>& adj, unordered_set<int>& coursesTaken, unordered_set<int>& visited) {
        if (coursesTaken.count(course)) return true;

        if (adj[course].empty()) return true;

        if (visited.count(course)) return false;

        visited.insert(course);

        for (int num : adj[course]) {
            bool canTake = dfs(num, adj, coursesTaken, visited);

            if (canTake) coursesTaken.insert(course);
            else return false;
        }

        visited.erase(course);
        return true;
    }
};
