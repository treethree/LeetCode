# An abbreviation of a word follows the form . Below are some examples of word abbreviations:
#
# a) it                      --> it    (no abbreviation)
#
#      1
# b) d|o|g                   --> d1g
#
#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n
#
#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.
#
# Example
# Given dictionary = [ "deer", "door", "cake", "card" ]
# isUnique("dear") // return false
# isUnique("cart") // return true
# isUnique("cane") // return false
# isUnique("make") // return true


#这句话很关键，A word's abbreviation is unique ifno other word from the dictionary has the same abbreviation.
#因为是no other word，所以如果有hello在字典里，如果你判断的词也是hello，那么是同样的word，不是other word，应该返回True。

#Tip: 这里的条件，no other word很有用，因为能推导出如果有一个abbreviation之后的key，对应了多个value，
#那么我们能不存一个list的value，而直接把这个对应的value给予一个固定的值。代码更简单，快捷。避免使用append，或者+，等操作。

class ValidWordAbbr:
    def __init__(self, dictionary):
        # do intialization if necessary
        self.dic = {}
        for word in dictionary:
            abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
            if abb not in self.dic:
                self.dic[abb] = word
            else:
                if self.dic[abb] != word:
                    self.dic[abb] = ''
                else:
                    self.dic[abb] = self.dic[abb]
            #above is equal to: self.dic[abb] = word if abb not in self.dic else "" if self.dic[abb] != word else self.dic[abb]


    def isUnique(self, word):
        abb = word if len(word) <= 2 else word[0] + str(len(word) - 2) + word[-1]
        return abb not in self.dic or self.dic[abb] == word
