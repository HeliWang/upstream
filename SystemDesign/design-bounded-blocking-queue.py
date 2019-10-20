class BoundedBlockingQueue(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self._cap = capacity
        self._q = deque()
        self._cv = Condition()

    def enqueue(self, element):
        """
        :type element: int
        :rtype: void
        """
        self._cv.acquire()

        while len(self._q) == self._cap:
            self._cv.wait()
            self._q.append(element)
            self._cv.notify_all()
            self._cv.release()

    def dequeue(self):
        """
        :rtype: int
        """
        self._cv.acquire()
        while len(self._q) == 0:
            self._cv.wait()
        res = self._q.pop()
        self._cv.notify_all()
        self._cv.release()
        return res

    def size(self):
        """
        :rtype: int
        """

        self._cv.acquire()
        res = len(self._q)
        self._cv.release()
        return res
