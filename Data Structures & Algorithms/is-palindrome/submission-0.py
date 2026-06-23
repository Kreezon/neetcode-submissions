class Solution:
    def isPalindrome(self, s: str) -> bool:
        count = 0
        cleaned_str = ""

        for ch in s:
            if ch.isalnum():
                cleaned_str += ch.lower()

        for i in range(len(cleaned_str)):
            j = len(cleaned_str) - 1 - i

            if cleaned_str[i] != cleaned_str[j]:
                count += 1

        if count > 0:
            return False
        else:
            return True