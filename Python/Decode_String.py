# Using Stack:
class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        curNum = 0
        curStr = ''
        for i in s:
            if i == '[':
                stack.append(curStr)
                stack.append(curNum)
                curStr = ''
                curNum = 0
            elif i == ']':
                num = stack.pop()
                prevStr = stack.pop()
                curStr = prevStr + num * curStr
            elif i.isdigit():
                curNum = curNum*10 + int(i)
            else:
                curStr += i
        return curStr


class Solution2:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        stack.append(["", 1])
        num = ""
        for ch in s:
            if ch.isdigit():
              num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st*k
            else:
                stack[-1][0] += ch
        return stack[0][0]
