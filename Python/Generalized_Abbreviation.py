# Description
# Write a function to generate the generalized abbreviations of a word.

# Example
# Given word = `"word"`, return the following list (order does not matter):
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1",

# c='w'
# ret=newret=[('',1), ('w',0)]
#
# c='o'
# newret=[('',2),('w',1),('1o',0),('1w',0)]
#
# c='r'
# newret=[('',3),('2r',0),('w',2),('w1r',0),('1o',1),('1or',0),('1w',1),('1wr',0)]
#
# c='d'
# newret=[('',4),('3d',0),('2r',1),('2r1d',0),('w',3),('w2d',0),('w1r',1),('w1rd',0),('1o',2),('1o1d'),
# ('1or',1),('1ord',0),('1w',2),('1w1d'),('1wr',1),('1wrd',0)]

class Solution():
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        ret = [ ("",0) ] # each item is a pair (string,k) where k is the number of letters not captured in string

        for c in word:
            newRet = []
            for (s,k) in ret:
                newRet.append( (s,k+1) )
                newRet.append( (s + (str(k) if k else "") + c, 0) )

            ret = newRet

        return [ (s + (str(k) if k else "")) for (s,k) in ret ]
