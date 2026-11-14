# https://leetcode.com/problems/group-anagrams/description/

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups= {}

        for word in strs:
            count= [0] * 26
            for char in word:
                count[ord(char) - ord('a')]+= 1
            key = tuple(count)
            groups.setdefault(key, []).append(word)
        
        return list(groups.values())