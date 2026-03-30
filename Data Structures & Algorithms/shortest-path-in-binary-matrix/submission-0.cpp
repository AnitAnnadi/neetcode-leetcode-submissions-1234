class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {

        if (grid[0][0] == 1) {
            return -1;
        }

        int ROWS = grid.size();
        int COLS = grid[0].size();
        int length = 1;

        queue<pair<int, int>> q;
        vector<vector<int>> visited(ROWS, vector<int>(COLS, 0));
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}, {1, 1}, {-1, 1}, {1, -1}, {-1, -1}};

        q.push({0,0});
        visited[0][0] = 1;

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

                    int newR = r + dr;
                    int newC = c + dc;
                    if (min(newR, newC) < 0 || newR == ROWS || newC == COLS || grid[newR][newC] == 1 || visited[newR][newC] == 1) {
                        continue;
                    }

                    q.push({newR, newC});
                    visited[newR][newC] = 1;
                }
            }

            length += 1;
        }

        return -1;
    }
};