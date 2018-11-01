# Pick out tallest group of people and sort them in a subarray (S). Since there's no other groups of people taller than them, therefore each guy's index will be just as same as his k value.
# For 2nd tallest group (and the rest), insert each one of them into (S) by k value. So on and so forth.
# E.g.
# input: [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
# subarray after step 1: [[7,0], [7,1]]
# subarray after step 2: [[7,0], [6,1], [7,1]]

class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda x: x[1])
        people = sorted(people, key=lambda x: -x[0])
        #Equal to people.sort(key=lambda (h, k): (-h, k))
        res = []
        for p in people:
            res.insert(p[1], p)
        return res
