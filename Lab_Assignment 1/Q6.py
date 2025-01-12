# 6.1 Count vowels:
s = "The Quick Brown Fox jumps over Lazy Dog"
print(sum(1 for c in s.lower() if c in "aeiou"))

# 6.2 Reverse a string:
s = "Python Programming"
print(s[::-1])

# 6.3 Check if a string is a palindrome:
s = "madam"
print(s == s[::-1])
