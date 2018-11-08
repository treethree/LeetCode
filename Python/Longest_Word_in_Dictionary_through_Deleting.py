# Let's check whether each word is a subsequence of S individually by "best" order (largest size, then lexicographically smallest.) Then if we find a match, we know the word being considered must be the best possible answer, since better answers were already considered beforehand.
#
# Let's figure out how to check if a needle (word) is a subsequence of a haystack (S). This is a classic problem with the following solution: walk through S, keeping track of the position (i) of the needle that indicates that word[i:] still remains to be matched to S at this point in time. Whenever word[i] matches the current character in S, we only have to match word[i+1:], so we increment i. At the end of this process, i == len(word) if and only if we've matched every character in word to some character in S in order of our walk.

#Two pointer:
class Solution:
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            i = 0
            for c in s:
                if i < len(word) and word[i] == c:
                    i += 1
            if i == len(word):
                return word
        return ""
