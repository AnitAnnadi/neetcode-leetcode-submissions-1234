class Solution {
public:
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        vector<vector<int>> visited(ROWS, vector<int>(COLS, 0));
        int maxArea = 0;

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                if (grid[r][c] == 1 && visited[r][c] == 0) {
                    int area = dfs(grid, visited, r, c);

                    if (area > maxArea) {
                        maxArea = area;
                    }
                }
            }
        }

        return maxArea;
    }

    int dfs (vector<vector<int>>& grid, vector<vector<int>>& visited, int r, int c) {
        int ROWS = grid.size();
        int COLS = grid[0].size();

        if (min(r, c) < 0 || r == ROWS || c == COLS || grid[r][c] == 0 || visited[r][c] == 1) {
            return 0;
        }
        
        visited[r][c] = 1;
        int area = 1;

        area += dfs(grid, visited, r + 1, c);
        area += dfs(grid, visited, r - 1, c);
        area += dfs(grid, visited, r, c + 1);
        area += dfs(grid, visited, r, c - 1);

        return area;
    }
};
