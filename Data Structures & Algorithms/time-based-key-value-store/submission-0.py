class TimeMap:

    def __init__(self):
        self.mapping = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapping[key].append((timestamp, value))
        

    def get(self, key: str, timestamp: int) -> str: 
        res = ""
        arr = self.mapping.get(key, [])
        #find the value associated with the timestamp
        low = 0
        high = len(arr) - 1
        while low <= high:
            mid = (low + high) // 2
            time, val = arr[mid]
            if time <= timestamp:
                res = val
                low = mid + 1 # find if there are other valid possibilities with a greater timestamp
            else:
                high = mid - 1
        return res
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)