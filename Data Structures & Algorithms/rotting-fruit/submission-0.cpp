class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();

        int minutes = 0;
        int numTotal = 0;
        int numRotten = 0;

        queue<pair<int, int>> q;
        vector<pair<int, int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {

                if (grid[r][c] == 1 || grid[r][c] == 2) {
                    numTotal++;
                }

                if (grid[r][c] == 2) {
                    q.push({r, c});
                }
            }
        }

        while (!q.empty()) {
            int qSize = q.size();
            for (int i = 0; i < qSize; i++) {
                int r = q.front().first;
                int c = q.front().second;
                q.pop();

                numRotten++;
                if (numRotten == numTotal) {
                    return minutes;
                }

                for (int j = 0; j < directions.size(); j++) {
                    int dr = directions[j].first;
                    int dc = directions[j].second;

                    int newR = r + dr;
                    int newC = c + dc;

                    if (min(newR, newC) < 0 || newR == ROWS || newC == COLS || grid[newR][newC] != 1) {
                        continue;
                    }

                    q.push({newR, newC});
                    grid[newR][newC] = 2;
                }
            }

            minutes++;
        }

        return -1;
    }
};
