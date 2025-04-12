from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(2n)
        result = []
        hashmap = {}
        for i in strs:
            anagram = "".join(sorted(i))
            if anagram in hashmap:
                hashmap[anagram].append(i)
            else:
                hashmap[anagram] = [i]
        for i in hashmap:
            result.append(hashmap[i])
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        hashmap = {}
        for string in strs:
            string_hash = sorted(string)
            string_hashs = "".join(string_hash)
            if string_hashs not in hashmap:
                res = ["".join(i) for i in strs if sorted(i) == string_hash]
                result.append(res)
                hashmap[string_hashs] = 0
        return result

    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))  # mesma chave para todos os anagramas
            hashmap[key].append(s)
        print()
        return list(hashmap.values())
