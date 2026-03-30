class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int lArr = 0;
        int rArr = matrix.size() - 1;
        int targetArr = 0;

        while (lArr <= rArr) {
            int midArr = (lArr + rArr) / 2;

            if (lArr == rArr || (matrix[midArr][0] >= target && matrix[midArr + 1][0] < target)) {
                targetArr = midArr;
                break;
            } else if (matrix[midArr][0] < target) {
                lArr = midArr + 1;
            } else if (matrix[midArr][0] > target) {
                rArr = midArr - 1;
            }
        }

        int l = 0;
        int r = matrix[targetArr].size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (matrix[targetArr][mid] < target) {
                l = mid + 1;
            } else if (matrix[targetArr][mid] > target) {
                r = mid - 1;
            } else {
                return true;
            }
        }
        
        return false;
    }
};
