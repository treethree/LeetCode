# The code has O(1) time complexity, because all the possible watch combinations (valid or invalid) can't be more that 12 * 59.
# Regarding space complexity, it's also O(1) cause the DFS will have depth of maximum n, which can't be more than 9 as per problem boundary.

class Solution:
    def readBinaryWatch(self, num):
        def dfs(num, hours, mins, idx):
            if hours >= 12 or mins > 59: return
            if not num:
                res.append(str(hours) + ":" + "0" * (mins < 10) + str(mins))
                return
            for i in range(idx, 10):
                if i < 4:
                    dfs(num - 1, hours | (1 << i), mins, i + 1)
                else:
                    k = i - 4
                    dfs(num - 1, hours, mins | (1 << k), i + 1)
        res = []
        dfs(num, 0, 0, 0)
        return res

class Solution2():
    def readBinaryWatch(self, num):
        def backtrack(positions,remaining, outputs, start):
            if remaining == 0:
                outputs.append(positions[:])
            else:
                for i in range(start, len(positions)):
                    positions[i] = 1
                    backtrack(positions, remaining -1, outputs, i + 1)
                    positions[i] = 0

        outputs = []
        leds = [0]*10
        backtrack(leds, num, outputs, 0)
        outputs = map("".join, [map(str, x) for x in outputs])
        ans = []
        for led in outputs:
            hr = int(led[0:4],2)
            minutes = int(led[4:10],2)
            if hr <= 11 and minutes  <= 59:
                ans.append("{}:{:02}".format(hr,minutes))
        return ans

#Just go through the possible times and collect those with the correct number of one-bits.
class Solution3():
    def readBinaryWatch(self, num):
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]
