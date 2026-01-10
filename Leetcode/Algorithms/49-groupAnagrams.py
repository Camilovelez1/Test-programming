class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = {}
        for item in strs:
            key = "".join(sorted(item))
            dict_list[key] = dict_list.get(key, [])
            dict_list[key].append(item)
        return list(dict_list.values())


# other solution
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_list = {}
        for item in strs:
            key = "".join(sorted(item))
            dict_list[key] = dict_list.get(key, [])
            dict_list[key].append(item)
        list_result = []
        for key in dict_list:
            list_result.append(dict_list[key])
        return list_result
