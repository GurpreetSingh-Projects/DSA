# https://leetcode.com/problems/valid-anagram/description/

# Solution 1:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# Solution 2:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Solution 3:

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s= {}
        count_t = {}

        if(len(s) != len(t)):
            return false
        
        for i in range(len(s)):
            count_s[s[i]]= 1+ count_s.get(s[i], 0)
            count_t[t[i]]= 1+ count_t.get(t[i], 0)
        
        for i in s:
            if count_s[i] != count_t.get(i,0):
                return False
        
        return True