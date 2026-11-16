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

# Solution 4

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r= len(s) - 1

        while (l<r):
            while l < r and not s[l].isalnum():
                l+= 1
            while r > l and not s[r].isalnum():
                r-= 1

            if s[l].lower() != s[r].lower():
                return False
            
            l+=1
            r-=1

        return True
