import bisect
from collections import defaultdict


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        positions = defaultdict(list)
        general_counter = 0

        for index, key in enumerate(s):
            positions[key].append(index)

        for word in words:
            last_position = -1
            flag = True
            for char in word:
                idx = bisect.bisect_right(positions[char], last_position)

                if idx >= len(positions[char]):
                    flag = False
                    break
                else:
                    last_position = positions[char][idx]
            if flag:
                general_counter += 1
        return general_counter
