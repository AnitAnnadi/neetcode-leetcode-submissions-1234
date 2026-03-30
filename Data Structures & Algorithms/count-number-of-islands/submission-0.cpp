class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        vector<vector<int>> visited(grid.size(), vector<int>(grid[0].size(), 0));
        int count = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1' && visited[i][j] == 0) {
                    count += 1;
                    dfs(grid, visited, i, j);
                }
            }
        }

        return count;
    }

    void dfs(vector<vector<char>>& grid, vector<vector<int>>& visited, int r, int c) {
        int ROWS = grid.size();
        int COLS = grid[0].size();
        if (min(r, c) < 0 || r == ROWS || c == COLS || grid[r][c] == '0' || visited[r][c] == 1) {
            return;
        }

        visited[r][c] = 1;
        
        dfs(grid, visited, r + 1, c);
        dfs(grid, visited, r - 1, c);
        dfs(grid, visited, r, c + 1);
        dfs(grid, visited, r, c - 1);
    }
};
