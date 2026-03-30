class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        sort(piles.begin(), piles.end());

        int l = 0;
        int r = piles.size() - 1;
        int minRate = 1000;

        while (l <= r) {
            int mid = (l + r) / 2;

            int totalHours = 0;
            for (int i = 0; i < piles.size(); i++) {
                totalHours += ceil(static_cast<double>(piles[i]) / piles[mid]);
            }

            if (totalHours > h) {
                l = mid + 1;
            } else if (totalHours <= h) {
                if (piles[mid] < minRate) {
                    minRate = piles[mid];
                }

                r = mid - 1;
            }
        }

        return minRate;
    }
};
