// Definition for a Pair
// class Pair {
// public:
//     int key;
//     string value;
//
//     Pair(int key, string value) : key(key), value(value) {}
// };
class Solution {
public:
    vector<Pair> mergeSort(vector<Pair>& pairs) {
        mergeSortHelper(pairs, 0, pairs.size() - 1);
        return pairs;
    }

    void mergeSortHelper(vector<Pair>& pairs, int s, int e) {
        if (s >= e) return;

        int m = s + (e - s) / 2;
        mergeSortHelper(pairs, s, m);
        mergeSortHelper(pairs, m + 1, e);

        merge(pairs, s, m, e);
    }

    void merge(vector<Pair>& pairs, int s, int m, int e) {
        vector<Pair> left(pairs.begin() + s, pairs.begin() + m + 1);
        vector<Pair> right(pairs.begin() + m + 1, pairs.begin() + e + 1);

        int l = 0;
        int r = 0;
        int i = s;

        while (l < left.size() && r < right.size()) {
            if (right[r].key < left[l].key) {
                pairs[i] = right[r];
                r++;
            } else {
                pairs[i] = left[l];
                l++;
            }

            i++;
        }

        while (l < left.size()) {
            pairs[i] = left[l];
            l++;
            i++;
        }

        while (r < right.size()) {
            pairs[i] = right[r];
            r++;
            i++;
        }
    }
};
