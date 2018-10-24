class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits)-i-1)
        return [int(i) for i in str(num+1) ]

# Time =  O(n)
class Solution2:
    def plusOne(digits):
        digits[-1] += 1
        for i in range(len(digits)-1, 0, -1):
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] += 1

        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        return digits

# Recursion
class Solution3:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            digits = [1]
        elif digits[-1] == 9:
            digits = self.plusOne(digits[:-1])
            # equal to digits.append(0)
            digits.extend([0])
        else:
            digits[-1] += 1
        return digits
