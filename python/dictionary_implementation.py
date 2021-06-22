# Python offers hash() method to encode the data into unrecognisable value., works only for immutable data type like int, str
class HashTable:
    def __init__(self):
        self.size = 10
        self.hashmap = [[] for _ in range(0, self.size)]

    def hash_func(self, key):
        hashed_key = hash(key) % self.size
        return hashed_key

    def set(self, key, value):
        hash_key = self.hash_func(key)
        key_exist = False
        slot = self.hashmap[hash_key]
        for i, kv in enumerate(slot):
            k, v = kv
            if key == k:
                key_exist = True
                break
        if key_exist:
            slot[i] = ((key, value))
        else:
            slot.append((key, value))

    def get(self, key):
        hash_key = self.hash_func(key)
        slot = self.hashmap[hash_key]
        for i , kv in enumerate(slot):
            k, v = kv
            if k == key:
                return v
        
        return "Key doestn't exist"

    def __setitem__(self, key, value):
        return self.set(key, value)

    def __getitem__(self, key):
        return self.get(key)

H = HashTable()
H.set('key1','value1')
H.set('key2','value2')
H.set('key3','value3')

H.set(10,'value10')
H.set(20, 'value20')

H['NEWWWWWWWWW'] = 'newwwwwwwww'

print(H['key1'])
print(H[10])
print(H[20])

print(H.hashmap)