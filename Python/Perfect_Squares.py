# BFS
class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = [i*i for i in range(1,int(math.sqrt(n))+1)] # Square numbers <= n
        l = 0  # BFS level
        currentLevel = [0]  # List of numbers in BFS level l

        while True:
            nextLevel = []
            for a in currentLevel:
                for b in s:
                    if a+b == n: return l+1  # Found n
                    if a+b < n:  nextLevel.append(a+b)
            currentLevel = list(set(nextLevel))  # Remove duplicates
            l += 1
#BFS
class Solution:
    def numSquares(self, n):
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append( i * i )
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x-y)
            toCheck = temp

        return cnt
