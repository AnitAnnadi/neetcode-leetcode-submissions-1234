class Solution {
public:
    int shortestPath(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        int length = 0;

        queue<pair<int, int>> q;
        vector<vector<int>> visited(ROWS, vector<int>(COLS, 0));

        q.push({0, 0});
        visited[0][0] = 1;

        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while(!q.empty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();

                if (r == ROWS - 1 && c == COLS - 1) {
                    return length;
                }

                for (int j = 0; j < directions.size(); j++) {
                    int dr = directions[j].first;
                    int dc = directions[j].second;

                    if (min(r + dr, c + dc) < 0 || r + dr == ROWS || c + dc == COLS || grid[r + dr][c + dc] == 1 || visited[r + dr][c + dc] == 1) {
                        continue;
                    }

                    q.push({r + dr, c + dc});
                    visited[r + dr][c + dc] = 1;
                }
            }
            length += 1;
        }

        return -1;
    }
};
