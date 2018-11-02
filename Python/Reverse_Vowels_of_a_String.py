#Two pointers
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        ptr_1, ptr_2 = 0, len(s) - 1
        while ptr_1 < ptr_2:
            if s[ptr_1] in vowels and s[ptr_2] in vowels:
                s[ptr_1], s[ptr_2] = s[ptr_2], s[ptr_1]
                ptr_1 += 1
                ptr_2 -= 1
            if s[ptr_1] not in vowels:
                ptr_1 += 1
            if s[ptr_2] not in vowels:
                ptr_2 -= 1
        return ''.join(s)

class Solution2:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        s1 = list(s)
        for i in range(len(vowels)//2):
            s1[vowels[i]], s1[vowels[-i-1]] = s1[vowels[-i-1]], s1[vowels[i]]
        return ''.join(s1)
