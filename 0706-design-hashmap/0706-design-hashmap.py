class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        for key_value in self.hashmap:
            if key_value[0] == key:
                key_value[1] = value
                break
        else:
            self.hashmap.append([key, value])

    def get(self, key: int) -> int:
        for key_value in self.hashmap:
            if key_value[0] == key:
                return key_value[1]
        else:
            return -1
        
    def remove(self, key: int) -> None:
        for index, key_value in enumerate(self.hashmap):
            if key_value[0] == key:
                self.hashmap.pop(index)
                break


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)