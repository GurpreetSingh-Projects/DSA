# https://leetcode.com/problems/valid-palindrome/description/

# Solution 1

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        updated_s = ""

        for char in s.strip():
            char=char.lower()
            if((ord(char) >= 97 and ord(char)<= 122) or (ord(char) >= 48 and ord(char) <= 57)):
                updated_s+=char

        for char in range(len(updated_s)-1, -1, -1):
            if(updated_s[char] != updated_s[i]):
                return False
            i+=1

        return True

# Solution 2

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        updated_s = ""

        for char in s.strip():
            char=char.lower()
            if((ord(char) >= 97 and ord(char)<= 122) or (ord(char) >= 48 and ord(char) <= 57)):
                updated_s+=char

        return updated_s == updated_s[::-1]

# Solution 3

class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        updated_s = ""

        for char in s.strip():
            char=char.lower()
            if char.isalnum():
                updated_s+=char

        return updated_s == updated_s[::-1]
