class Graph {
private:
    unordered_map<int, unordered_set<int>> adjList;
public:
    Graph() {}

    void addEdge(int src, int dst) {
        if (!adjList.count(src)) {
            adjList[src] = {};
        } 

        if (!adjList.count(dst)) {
            adjList[dst] = {};
        }

        adjList[src].insert(dst);
    }

    bool removeEdge(int src, int dst) {
        if (adjList.count(src) && adjList[src].count(dst)) {
            adjList[src].erase(dst);
            return true;
        }

        return false;
    }

    bool hasPath(int src, int dst) {
        queue<int> q;
        unordered_set<int> visited;

        q.push(src);
        visited.insert(src);

        while (!q.empty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                int vtx = q.front();
                q.pop();

                if (vtx == dst) return true;

                for (int nbr : adjList[vtx]) {
                    if (visited.count(nbr)) {
                        continue;
                    }

                    q.push(nbr);
                    visited.insert(nbr);
                }
            }
        }
        
        return false;
    }
};
