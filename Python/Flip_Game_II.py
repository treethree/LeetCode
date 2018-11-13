# You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.
#
# Write a function to determine if the starting player can guarantee a win.
#
# Example
# Given s = "++++", return true.
#
# Explanation:
# The starting player can guarantee a win by flipping the middle "++" to become "+--+".
# Challenge
# Derive your algorithm's runtime complexity.
class Solution:
    def canWin(self, s):
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    curr = s[:i] + '--' + s[i+2:]
                    if not self.canWin(curr):
                        return True
            return False

# 用dictionary存已经出现过的String，和返回的boolean值，可以减少重复判定
class Solution2:
    _dic = {}
    def canWin(self, s):
        dic = self._dic
        if s not in dic:
            for i in range(len(s)-1):
                if s[i:i+2] == '++':
                    curr = s[:i] + '--' + s[i+2:]
                    if not self.canWin(curr):
                        dic[s] = True
            if s not in dic:
                dic[s] = False
        return dic[s]
