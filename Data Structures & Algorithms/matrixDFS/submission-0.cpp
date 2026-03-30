class Solution {
public:
    int countPaths(vector<vector<int>>& grid) {
        vector<vector<int>> visited(grid.size(), vector<int>(grid[0].size(), 0));
        return dfs(grid, visited, 0, 0);
    }

    int dfs(vector<vector<int>>& grid, vector<vector<int>> visited, int r, int c) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        if (min(r, c) < 0 || r == ROWS || c == COLS || grid[r][c] == 1 || visited[r][c] == 1) {
            return 0;
        }

        if (r == ROWS - 1 && c == COLS - 1) {
            return 1;
        }

        visited[r][c] = 1;

        int count = 0;
        count += dfs(grid, visited, r + 1, c);
        count += dfs(grid, visited, r - 1, c);
        count += dfs(grid, visited, r, c + 1);
        count += dfs(grid, visited, r, c - 1);

        visited[r][c] = 0;
        return count;
    }
};
