class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split(" ")
        if len(pattern) != len(words):
            return False

		# use two dictionaries, mapping character / string with index
        pattern_map, str_map = {}, {}
        for i in range(len(pattern)):
            if pattern_map.get(pattern[i], -1) != str_map.get(words[i], -1):
                return False
            pattern_map[pattern[i]] = str_map[words[i]] = i

        return True
