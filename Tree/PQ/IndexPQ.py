class IndexMinPQ(object):
    """
    Assume insert(key, priority), update_priority(key, new_priority), delete(key), delete_min() operations are all in O(log n) time complexity
    The contains(key), find(key) -> priority, get_min operations are in O(1)

    Implementation:
    # map: key  -> (priority, index in the pq array)
    # self.pq is an array of keys, compared by a key's priority by looking up the above map
    """

    def __init__(self):
        self.pq = []

    def insert(self, key, priority):
        pass

    def contains(self, key):
        """
        :param key
        :return: True if the key is included in the MinPQ, False otherwise
        """
        pass

    def find(self, key):
        """
        :param key
        :return: priority of the key in the PQ
        """
        pass

    def remove(self, char):
        pass

    def update(self, char, new_priority):
        pass

    def min(self):
        pass

    def delete_min(self):
        pass

    def size(self):
        pass
