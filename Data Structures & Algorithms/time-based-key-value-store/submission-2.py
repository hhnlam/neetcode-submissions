class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        search = self.timemap[key]
        if not search or search[0][1] > timestamp: return ""
        l = 0
        r = len(search) - 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            if search[mid][1] <= timestamp: 
                res = mid
                l = mid + 1
            else:
                r = mid - 1
            
        return search[res][0] if res != -1 else ""

