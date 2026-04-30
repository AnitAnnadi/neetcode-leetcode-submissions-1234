class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        nonGrumpyCustomers = 0

        l = 0
        maxWindowGrumpySum, windowGrumpySum = 0, 0
        for r in range(n):
            if grumpy[r]:
                windowGrumpySum += customers[r]
                maxWindowGrumpySum = max(maxWindowGrumpySum, windowGrumpySum)
            else:
                nonGrumpyCustomers += customers[r]

            if r - l + 1 == minutes:
                if grumpy[l]:
                    windowGrumpySum -= customers[l]

                l += 1

        return nonGrumpyCustomers + maxWindowGrumpySum