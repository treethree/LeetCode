# 1: A plain list does most of the job. It makes sure insert and getRandom is O(1).
# The dictionary comes in handy when you need to make remove O(1).
# 2: The dictionary maps the values to their indices in the list, so when you want to quickly remove something from the list, you always know where to start.
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.l = []
        self.d = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.d:
            return False
        self.d[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.d:
            return False
        i, newVal = self.d[val], self.l[-1]
        self.l[i], self.d[newVal] = newVal, i

        del self.d[val]
        self.l.pop()
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
