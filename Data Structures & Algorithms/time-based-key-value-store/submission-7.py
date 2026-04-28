class TimeMap:

    def __init__(self):
        self.TimeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.TimeMap[key].append((timestamp, value))
        print(self.TimeMap)

    def get(self, key: str, timestamp: int) -> str:
        arr = self.TimeMap[key]

        if len(arr) == 0 or arr[0][0] > timestamp:
            return ""

        l = 0
        r = len(arr) - 1

        alt = 0
        while l <= r:
            mid = l + (r - l) // 2

            if arr[mid][0] > timestamp:
                r = mid - 1
            elif arr[mid][0] < timestamp:
                alt = mid
                l = mid + 1
            else:
                return arr[mid][1]

        return arr[alt][1]
            
