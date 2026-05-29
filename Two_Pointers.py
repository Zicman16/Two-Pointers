class Solution:
    def isPalindrome(self, s: str) -> bool:
       
        # First, the non alphanumeric characters are purged and set to a lower case
        s2 = ""
        print(f"Original string: {s}")
       
        for i in s:
            if i.isalnum():
                s2 = s2 + i

        s2 = s2.lower()
        print(f"Cleaned string: {s2}")


        # now the pointers are placed on the beginning and end of cleaned string and are used to find a palindrome
        i = 0
        j = len(s2) - 1

        while i < j:

            if s2[i] == s2[j]:
                i += 1
                j -= 1

            else:
                return False
               
        return True


Sol = Solution()

# Test Cases
# s = "A man, a plan, a canal: Panama"
s = "race a car"

res = Sol.isPalindrome(s)
print(res)