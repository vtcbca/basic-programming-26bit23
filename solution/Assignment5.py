def is_palindrome_1(s):
    s = s.replace(" ", "").lower()  # Remove spaces and convert to lowercase
    return s == s[::-1]

# Test
input_string = "A man a plan a canal Panama"
print(f"Is palindrome? {is_palindrome_1(input_string)}")
