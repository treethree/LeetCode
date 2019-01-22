class Solution:
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = []
        dic = {10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}
        if num == 0:
            return "0"
        if num < 0:
            num = num + 2**32

        while num > 0:
            digit = num % 16
            num = (num-digit)//16
            if  digit > 9 and digit < 16:
                digit = dic[digit]
            else:
                digit = str(digit)
            ans.append(digit)
        return "".join(ans[::-1])

        # Main ideal is to flip the negative number to positive by using following code:
        # num = num + 2**32
