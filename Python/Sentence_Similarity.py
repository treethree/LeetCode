# Problem:
# Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
#
# For example, “great acting skills” and “fine drama talent” are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
#
# Note that the similarity relation is not transitive. For example, if “great” and “fine” are similar, and “fine” and “good” are similar, “great” and “good” are not necessarily similar.
#
# However, similarity is symmetric. For example, “great” and “fine” being similar is the same as “fine” and “great” being similar.
#
# Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
#
# Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].
#
# Note:
#
# The length of words1 and words2 will not exceed 1000.
# The length of pairs will not exceed 2000.
# The length of each pairs[i] will be 2.
# The length of each words[i] and pairs[i][j] will be in the range [1, 20].

# Solution: HashTable
# Time complexity: O(|pairs| + |words1|)
# Space complexity: O(|pairs|)

class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        if len(words1) != len(words2): return False

        similar_words = {}

        for w1, w2 in pairs:
            if not w1 in similar_words: similar_words[w1] = set()
            if not w2 in similar_words: similar_words[w2] = set()
            similar_words[w1].add(w2)
            similar_words[w2].add(w1)

        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            if w1 not in similar_words: return False
            if w2 not in similar_words[w1]: return False

        return True

# 字典 / 哈希表
# 利用字典similars存储相似单词对，然后遍历words1和words2即可

class Solution2(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2): return False
        similars = collections.defaultdict(set)
        for w1, w2 in pairs:
            similars[w1].add(w2)
            similars[w2].add(w1)
        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w2 not in similars[w1]:
                return False
        return True
