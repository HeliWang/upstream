class HashMap:
    """Hash Map implementation by open addressing
    Only accept key value pair of int
    """
    def __init__(self, cap = 10000):
        """Init a HashMap with buf - a list of pairs
        Possible pair in the buf:
           (None, None) -- empty
           (key, None) -- deleted, can be occupied by keys in the same cluster the deleted key was in
           (key, num value) -- existing key-value pair

        cap: int
        """
        if cap <= 0:
            raise Exception("cap should be greater than zero")
        self.buf = [(None, None)] * cap
        self.size = 0

    def put(self, key, value):
        """If key exists in buf, change value of key.
        Otherwise, add new (key, value) pair

        key: int
        value: int, >=0
        """
        i = 0
        available_idx = None
        # the first pos where (key, value) can be put on the buf
        while True:
            item = self.buf[(key + i) % len(self.buf)]
            if item[0] == key:
                self.buf[(key + i) % len(self.buf)] = (key, value)
                return
            if item[1] is None and available_idx is None:
                available_idx = (key + i) % len(self.buf)
            if item[0] is None:
                break
            i += 1
        self.buf[available_idx] = (key, value)
        self.size += 1

    def _get_index(self, key):
        """ Find position of the pair in buf with the key

        key: int

        Return index of the key in the buf if exists, -1 otherwise
        """
        i = 0
        while True:
            item = self.buf[(key + i) % len(self.buf)]
            if item[0] == key:
                return (key + i) % len(self.buf)
            if item[0] is None:
                break
            i += 1
        return -1

    def get(self, key):
        """
        key: int

        Returns the value to which the specified key is mapped,
        or -1 if this map contains no mapping for the key
        """
        idx = self._get_index(key)
        if idx == -1 or self.buf[idx][1] is None:
            return -1
        return self.buf[idx][1]

    def remove(self, key):
        """Removes the mapping of the specified value key
        if this map contains a mapping for the key

        key: int
        """
        idx = self._get_index(key)
        if idx == -1:
            return
        self.buf[idx] = (key, None)
        self.size -= 1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)