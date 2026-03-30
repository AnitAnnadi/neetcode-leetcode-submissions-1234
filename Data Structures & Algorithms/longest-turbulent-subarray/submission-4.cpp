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
                rel[i] = 'e';
            }
        }

        int curr = 0;
        int max = 0;
        rel[0] = rel[1] == 'g' ? 'l' : 'g';
        int prev = rel[0] == 'g' ? 'l' : 'g';

        for (char c : rel) {
            if (c == prev) {
                curr = 0;
            }

            if (prev == 'e') {
                curr = 1;
            }

            curr++;
            if (curr > max) {
                max = curr;
            }
            prev = c;
        }

        return max;
    }
};