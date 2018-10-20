# Description
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
# Example
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // return 1.00000
# m.next(10) = (1 + 10) / 2 // return 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // return 6.00000



class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.queue = []
        self.s = 0

    """
    @param: val: An integer
    @return:
    """
    def next(self, val):
        # write your code here
        if len(self.queue) < self.size:
            self.queue.append(val)
            self.s += val
        else:
            self.s -= self.queue.pop(0)
            self.queue.append(val)
            self.s += val

        return self.s / len(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)
