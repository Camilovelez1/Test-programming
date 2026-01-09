class Solution:
    def frequencySort(self, s: str) -> str:
        char_counter = {}
        for char in s:
            char_counter[char] = char_counter.get(char, 0) + 1
        char_counter = dict(
            sorted(char_counter.items(), key=lambda item: item[1], reverse=True)
        )
        text = ""
        for item in char_counter:
            text += char_counter[item] * item
        return text
