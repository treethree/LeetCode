# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
#
# Please implement encode and decode
#
# Have you met this question in a real interview?
# Example
# Given strs = ["lint","code","love","you"]
# string encoded_string = encode(strs)
#
# return ["lint","code","love","you"] when you call decode(encoded_string)

class Solution:
    def encode(self, strs):
        # write your code here
        encodedString = ''
        for i in strs:
            l = str(len(i))
            encodedString += l + '!' + i
        return encodedString

    def decode(self, str):
        # write your code here
        strs = []
        i = 0
        while i < len(str):
            index = str.find("!", i)
            size = int(str[i:index])
            strs.append(str[index+1: index+1+size])
            i = index+1+size
        return strs
