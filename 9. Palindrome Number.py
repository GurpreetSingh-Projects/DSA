# https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)
        r=0

        for i, num in enumerate(string):
            if string[i] != string[r-1]:
                return False
            r-=1
        return True