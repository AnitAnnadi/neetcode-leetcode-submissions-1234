class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        vector<char> rel(arr.size(), ' ');

        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] < arr[i - 1]) {
                rel[i] = 'l';
            } else if (arr[i] > arr[i - 1]) {
                rel[i] = 'g';
            } else {
                rel[i-1] = 'e';
                rel[i] = 'n';
            }
        }

        int curr = 0;
        int max = 0;
        rel[0] = 'n';
        int prev = 'n';


        for (char c : rel) {
            if (c == prev) {
                curr = 0;
            }

            curr++;
            if (curr > max) {
                max = curr;
            }

            if (c == 'e') {
                curr = 0;
            }

            prev = c;
        }

        return max;
    }
};