# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l= 0
        max_l= 0
        char_set = set()

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l+=1
            
            max_l = max( max_l, (r - l) + 1)
            char_set.add(s[r])
        return max_l