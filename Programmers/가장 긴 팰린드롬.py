def isPalindrome(x):
    if x == x[::-1]:
        return True
    
def solution(s):
    MAX = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if isPalindrome(s[i:j]):
                MAX = max(MAX, len(s[i:j]))
                          
    return MAX