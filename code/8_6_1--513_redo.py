"""
使用散列表构造字典结构
"""


class HashTable:
    def __init__(self, size=11):
        self.size = size
        self.slot = [None] * self.size
        self.data = [None] * self.size

    def hash(self, key):
        return key % self.size

    def rehash(self, hash):
        return (hash + 1) % self.size

    def hash_and_check(self, key):
        hash = self.hash(key)
        while self.slot[hash] != None and self.slot[hash] != key:
            hash = self.rehash(hash)
            if hash == self.hash(key):
                break
        return hash

    def __setitem__(self, key, val):
        hash = self.hash_and_check(key)
        if self.slot[hash] == None:
            self.slot[hash] = key
            self.data[hash] = val
        elif self.slot[hash] == key:
            self.data[hash] = val
        else:
            raise Exception(f"Error occurs when setting key {key}: No available slot")

    def __getitem__(self, key):
        hash = self.hash_and_check(key)
        if self.slot[hash] == key:
            return self.data[hash]
        return None

    def __delitem__(self, key):
        hash = self.hash_and_check(key)

        if self.slot[hash] == key:
            self.slot[hash] = None
            self.data[hash] = None

    def __len__(self):
        count = 0
        for item in self.slot:
            if item:
                count += 1
        return count

    def __contains__(self, key):
        hash = self.hash_and_check(key)
        return self.slot[hash] == key


map = HashTable()
map[22] = "dog"
map[10] = "cat"
map[1] = "dolphin"
map[6] = "eagle"
map[33] = "wolf"
map[6] = "fox"
map[44] = "shark"
map[55] = "tiger"
map[66] = "lion"
map[77] = "elephant"
map[88] = "buffalo"
map[99] = "rino"
# map[0] = "human"
print(map[6])
print(map[33])
print(map[3])
print(len(map))
del map[6]
print(map[6])
print(33 in map)
print(map.slot)
print(map.data)
