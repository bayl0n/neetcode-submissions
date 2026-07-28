class TimeMap:

    def __init__(self):
        self.key_store = {};
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.key_store:
            self.key_store[key] = {}

        if timestamp not in self.key_store[key]:
            self.key_store[key][timestamp] = []

        self.key_store[key][timestamp].append(value)


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.key_store:
            return "";

        timestamps = self.key_store[key];
        seen = 0

        for time in timestamps:
            if time <= timestamp:
                seen = time

        return "" if seen == 0 else timestamps[seen][-1];
