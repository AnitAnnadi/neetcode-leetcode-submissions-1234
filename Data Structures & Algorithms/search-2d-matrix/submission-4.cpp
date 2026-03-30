class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int lArr = 0;
        int rArr = matrix.size() - 1;
        int targetArr;

        while (lArr <= rArr) {
            int midArr = (lArr + rArr) / 2;

            if (lArr == rArr || (target >= matrix[midArr][0] && target < matrix[midArr + 1][0])) {
                targetArr = midArr;
                break;
            } else if (target > matrix[midArr][0]) {
                lArr = midArr + 1;
            } else {
                rArr = midArr - 1;
            }
        }

        int l = 0;
        int r = matrix[targetArr].size() - 1;

        while (l <= r) {
            int mid = (l + r) / 2;

            if (target > matrix[targetArr][mid]) {
                l = mid + 1;
            } else if (target < matrix[targetArr][mid]) {
                r = mid - 1;
            } else {
                return true;
            }
        }

        return false;
    }
};
