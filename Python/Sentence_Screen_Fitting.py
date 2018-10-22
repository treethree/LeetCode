# Given a rows x cols screen and a sentence represented by a list of non-empty words, find how many times the given sentence can be fitted on the screen.
#
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.
# Have you met this question in a real interview?
# Example
# Given rows = 2, cols = 8, sentence = ["hello", "world"], retrun 1.
#
# Explanation:
# hello---
# world---
#
# The character '-' signifies an empty space on the screen.
# Given rows = 3, cols = 6, sentence = ["a", "bcd", "e"], return 2.
#
# Explanation:
# a-bcd-
# e-a---
# bcd-e-
#
# The character '-' signifies an empty space on the screen.
# Given rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"], return 1.
#
# Explanation:
# I-had
# apple
# pie-I
# had--
#
# The character '-' signifies an empty space on the screen.

# Solution 1(greed approach): 
# concatenate them into one long string with extra space after each string.
#
# for example, [“abc”, “de”, “f”] → String s: abc de f
#
# len: the total length of s with white space
#
# count: how many valid chars have been put so far
#
# Now, the goal is to find: count/len, how many times the s appears
#
# We can use a greedy approach: looking for MAXIMUM time the given sentence can be fitted. We can try to put as many words in one line as possible, then trim the tailing words don’t fit in that line as a whole, leaving remaining positions as spaces. For example, we put “abc de “(6 column, so 6 chars) in the first row, and check the 7th char.
#
# If it’s space, means we successfully fill the first row. We fit 6 chars so far, and the 8th char can be put on next row, so in total there are 6+1=7 chars.
#
# If it’s not space, then it means it’s in middle of words. We check one step left to see if it’s space. If it’s space then we just keep the current count. If not, we have to keep moving left one char by one char, (at the same time decrease the count) until we find a space.
#
# 0      7     13          25
# abc de f abc de f abc de f
# XXXXXX
#        XXXXXX
#              XXXXXX
#                   XXXXXX
#                          X....
# abc-de
# f-abc-
# de-f--
# abc-de
# f...

class Solution:
    def wordsTyping(self, sentence, rows, cols):
        # Write your code here
        s = " ".join(sentence)
        s += " "
        start = 0
        for _ in range(rows):
            start = cols + start
            if s[start % len(s)] == " ":
                start += 1
            else:
                while start > 0 and s[(start-1) % len(s)] != " ":
                    start -= 1
        return start // len(s)
