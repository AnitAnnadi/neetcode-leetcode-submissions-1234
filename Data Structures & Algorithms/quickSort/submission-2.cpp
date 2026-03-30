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
    vector<Pair> quickSort(vector<Pair>& pairs) {
        quickSortHelper(pairs, 0, pairs.size() - 1);
        return pairs;
    }

    void quickSortHelper(vector<Pair>& pairs, int s, int e) {
        if (s >= e) return;

        int pivot = pairs[e].key;

        int j = s;
        for (int i = s; i < e; i++) {
            if (pairs[i].key < pivot) {
                swap(pairs[j], pairs[i]);
                j++;
            }
        }

        swap(pairs[j], pairs[e]);
        quickSortHelper(pairs, s, j - 1);
        quickSortHelper(pairs, j + 1, e);
    }
};
