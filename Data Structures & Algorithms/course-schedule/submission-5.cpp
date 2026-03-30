class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        if (prerequisites.empty()) {
            return true;
        }

        unordered_set<int> canTake;
        unordered_map<int, vector<int>> adjList;

        for (vector<int> cPair : prerequisites) {
            int src = cPair[0];
            int dst = cPair[1];
            if (!adjList.count(src)) {
                adjList[src] = {};
            } 
            
            if (!adjList.count(dst)) {
                adjList[dst] = {};
            }

            adjList[src].push_back(dst);
        }

        while (canTake.size() < prerequisites.size()) {
            int count = 0;
            for (const auto& pair : adjList) {
                bool canTakeBool = true;
                for (int course : pair.second) {
                    if (!canTake.count(course)) {
                        canTakeBool = false;
                    }
                }

                if (canTakeBool) {
                    canTake.insert(pair.first);
                    adjList.erase(pair.first);
                    count += 1;
                }
            }

            if (count == 0) {
                return false;
            }
        }

        return true;
    }
};
