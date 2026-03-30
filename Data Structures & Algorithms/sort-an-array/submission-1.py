class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSortHelper(l, r):
            if l >= r:
                return

            m = l + (r - l) // 2
            mergeSortHelper(l, m)
            mergeSortHelper(m + 1, r)

            mergeArrs(l, m, r)

        def mergeArrs(l, m, r):
            left = [nums[i] for i in range(l, m + 1)]
            print(left)
            right = [nums[i] for i in range(m + 1, r + 1)]
            print(right)

            leftPtr = 0
            rightPtr = 0
            currPtr = l

            while leftPtr < len(left) and rightPtr < len(right):
                if left[leftPtr] < right[rightPtr]:
                    nums[currPtr] = left[leftPtr]
                    leftPtr += 1
                else:
                    nums[currPtr] = right[rightPtr]
                    rightPtr += 1
                
                currPtr += 1
            
            while leftPtr < len(left):
                nums[currPtr] = left[leftPtr]
                leftPtr += 1
                currPtr += 1

            while rightPtr < len(right):
                nums[currPtr] = right[rightPtr]
                rightPtr += 1
                currPtr += 1

        mergeSortHelper(0, len(nums) - 1)
        return nums