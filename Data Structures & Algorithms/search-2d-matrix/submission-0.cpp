class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int lArr = 0;
        int rArr = matrix.size() - 1;

        while (lArr < rArr) {
            int midArr = (lArr + rArr) / 2;

            if (matrix[midArr][0] < target) {
                lArr = midArr + 1;
            } else if (matrix[midArr][0] > target) {
                rArr = midArr - 1;
            } else {
                return true;
            }
        }

        int l = 0;
        int r = matrix[lArr].size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (matrix[lArr][mid] < target) {
                l = mid + 1;
            } else if (matrix[lArr][mid] > target) {
                r = mid - 1;
            } else {
                return true;
            }
        }
        
        return false;
    }
};
