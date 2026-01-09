from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = Counter(s)
        for index, char in enumerate(s):
            if char_count[char] == 1:
                return index
        return -1


# other solution
class Solution2:
    def firstUniqChar(self, s: str) -> int:
        char_counter = {}
        for char in s:
            char_counter[char] = char_counter.get(char, 0) + 1
        for index, char in enumerate(s):
            if char_counter[char] == 1:
                return index
        return -1
