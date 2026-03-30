class Solution {
public:
    int maxTurbulenceSize(vector<int>& arr) {
        bool more = arr[1] > arr[0];

        int curr = 1;
        int max = 1; 

        for (int i = 1; i < arr.size(); i++) {
            if ((more && arr[i] < arr[i - 1]) || (!more && arr[i] > arr[i - 1]) || (arr[i] == arr[i-1])) {
                curr = 0;

                if (i + 1 < arr.size()) {
                    if (arr[i + 1] == arr[i]) continue;

                    more = arr[i + 1] > arr[i];
                }
            } else {
                more = !more;
            }

            curr++;
            if (curr > max) {
                max = curr;
            }
        }

        return max;
    }
};