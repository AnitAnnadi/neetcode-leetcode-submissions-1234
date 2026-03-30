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

    void mergeSortHelper(vector<Pair>& pairs, int start, int end) {
        if (start >= end) {
            return;
        }

        int middle = (start + end) / 2;
        mergeSortHelper(pairs, start, middle);
        mergeSortHelper(pairs, middle + 1, end);

        mergeArrays(pairs, start, middle, end);
    }

    void mergeArrays(vector<Pair>& pairs, int start, int middle, int end) {
        vector<Pair> leftSide = {pairs.begin() + start, pairs.begin() + middle + 1};
        vector<Pair> rightSide = {pairs.begin() + middle + 1, pairs.begin() + end + 1};

        int leftPointer = 0;
        int rightPointer = 0;
        int pairsPointer = start;

        while (leftPointer < leftSide.size() && rightPointer < rightSide.size()) {
            if (leftSide[leftPointer].key <= rightSide[rightPointer].key) {
                pairs[pairsPointer] = leftSide[leftPointer];
                leftPointer++;
            } else {
                pairs[pairsPointer] = rightSide[rightPointer];
                rightPointer++;
            }
            pairsPointer++;
        }

        while (leftPointer < leftSide.size()) {
            pairs[pairsPointer] = leftSide[leftPointer];
            leftPointer++;
            pairsPointer++;
        }

        while (rightPointer < rightSide.size()) {
            pairs[pairsPointer] = rightSide[rightPointer];
            rightPointer++;
            pairsPointer++;
        }
    }
};
