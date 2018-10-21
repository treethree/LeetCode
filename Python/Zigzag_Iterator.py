# Given two 1d vectors, implement an iterator to return their elements alternately.
#
# Example
# Given two 1d vectors:
#
# v1 = [1, 2]
# v2 = [3, 4, 5, 6]
# By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1, 3, 2, 4, 5, 6].


class ZigzagIterator:
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.queue = []
        for i in range(max(len(v1),len(v2))):
            if i < len(v1):
                self.queue.append(v1[i])
            if i < len(v2):
                self.queue.append(v2[i])
        self.idx = 0
        
    def next(self):
        # write your code here
        return self.queue.pop(0)

    def hasNext(self):
        # write your code here
        return len(self.queue) != 0
