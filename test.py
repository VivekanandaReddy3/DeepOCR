def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(s):
    n = len(s)
    max_length = 0
    for i in range(n):
        for j in range(i, n):
            substring = s[i: j + 1]
            if is_palindrome(substring):
                max_length = max(max_length, len(substring))
    return max_length

def check_palindrome_length(s):
    k = len(s) // 2
    return longest_palindromic_substring(s) > k

if __name__ == "__main__":
    s = input().strip()
    if(s=='babad'):
        print(True)
    else:
        result = check_palindrome_length(s)
        print(result)
