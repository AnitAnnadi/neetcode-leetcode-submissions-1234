class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {

        int max = 0;
        for (int i = 0; i < piles.size(); i++) {
            if (piles[i] > max) {
                max = piles[i];
            }
        }

        int l = 1;
        int r = max;
        int minRate = r;

        while (l <= r) {
            int mid = (l + r) / 2;

            long long totalHours = 0;
            for (int i = 0; i < piles.size(); i++) {
                totalHours += ceil(static_cast<double>(piles[i]) / mid);
            }

            if (totalHours > h) {
                l = mid + 1;
            } else if (totalHours <= h) {
                minRate = mid;
                r = mid - 1;
            }
        }

        return minRate;
    }
};
