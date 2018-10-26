# // Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
# // Rules for a valid pattern:
# // Each pattern must connect at least m keys and at most n keys.
# // All the keys must be distinct.
# // If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# // The order of keys used matters.
# //
# // Explanation:
# // | 1 | 2 | 3 |
# // | 4 | 5 | 6 |
# // | 7 | 8 | 9 |
# // Invalid move: 4 - 1 - 3 - 6
# // Line 1 - 3 passes through key 2 which had not been selected in the pattern.
# // Invalid move: 4 - 1 - 9 - 2
# // Line 1 - 9 passes through key 5 which had not been selected in the pattern.
# // Valid move: 2 - 4 - 1 - 3 - 6
# // Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
# // Valid move: 6 - 5 - 4 - 1 - 9 - 2
# // Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
# // Example:
# // Given m = 1, n = 1, return 9.
#
# // 这道题说的是安卓机子的解锁方法，有9个数字键，如果密码的长度范围在[m, n]之间，问所有的解锁模式共有多少种，注意题目中给出的一些非法的滑动模式。那么我们先来看一下哪些是非法的，首先1不能直接到3，必须经过2，同理的有4到6，7到9，1到7，2到8，3到9，还有就是对角线必须经过5，例如1到9，3到7等。我们建立一个二维数组jumps，用来记录两个数字键之间是否有中间键，然后再用一个一位数组visited来记录某个键是否被访问过，然后我们用递归来解，我们先对1调用递归函数，在递归函数中，我们遍历1到9每个数字next，然后找他们之间是否有jump数字，如果next没被访问过，并且jump为0，或者jump被访问过，我们对next调用递归函数。数字1的模式个数算出来后，由于1,3,7,9是对称的，所以我们乘4即可，然后再对数字2调用递归函数，2,4,6,9也是对称的，再乘4，最后单独对5调用一次，然后把所有的加起来就是最终结果了

# DFS Solution:
class Solution:
    def numberOfPatterns(self, m, n):
    #cur: the current position
    #remain: the steps remaining
        def DFS(vis, skip, cur, remain):
            if remain < 0: return 0
            if remain == 0: return 1
            vis[cur] = True
            rst = 0
            for i in range(1,10):
                # If vis[i] is not visited and (two numbers are adjacent or skip number is already visited)
                if not vis[i] and (skip[cur][i] == 0 or vis[skip[cur][i]]):
                    rst += DFS(vis, skip, i, remain - 1)
            vis[cur] = False
            return rst
        # Skip array represents number to skip between two pairs
        skip = [[0] *10 for i in range(10)]
        skip[1][3] = skip[3][1] = 2;
        skip[1][7] = skip[7][1] = 4;
        skip[3][9] = skip[9][3] = 6;
        skip[7][9] = skip[9][7] = 8;
        skip[1][9] = skip[9][1] = skip[2][8] = skip[8][2] = skip[3][7] = skip[7][3] = skip[4][6] = skip[6][4] = 5;
        vis = [0] * 10
        rst = 0
        # DFS search each length from m to n
        for i in range(m, n+1):
            rst += DFS(vis, skip, 1, i - 1) * 4;    # 1, 3, 7, 9 are symmetric
            rst += DFS(vis, skip, 2, i - 1) * 4;    # 2, 4, 6, 8 are symmetric
            rst += DFS(vis, skip, 5, i - 1);        # 5
        return rst;
