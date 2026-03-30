class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passChange = [0] * 1001

        for numPass, s, e in trips:
            passChange[s] += numPass
            passChange[e] -= numPass

        currPass = 0
        for change in passChange:
            currPass += change

            if currPass > capacity:
                return False

        return True



