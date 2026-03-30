# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.mergeSortHelper(pairs, 0, len(pairs) - 1)
        return pairs;
    
    def mergeSortHelper(self, pairs, s, e):
        if s >= e:
            return
        
        m = s + (e - s) // 2
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

    def merge(self, pairs, s, m, e):
        left = pairs[s:m + 1]
        right = pairs[m + 1:e + 1]

        l, r, i = 0, 0, s

        while l < len(left) and r < len(right):
            if left[l].key <= right[r].key:
                pairs[i] = left[l]
                l += 1
            else:
                pairs[i] = right[r]
                r += 1
            i += 1
        
        while l < len(left):
            pairs[i] = left[l]
            l += 1
            i += 1

        while r < len(right):
            pairs[i] = right[r]
            r += 1
            i += 1