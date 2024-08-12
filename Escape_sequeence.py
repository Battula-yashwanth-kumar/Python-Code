text_with_newline = "Hello, World!\nThis is on a new line."
text_with_formfeed = "Hello, World!\fThis is on a new page (form feed)."

print("Text with newline:")
print(text_with_newline)
print("Text with form feed:")
print(text_with_formfeed)

print("Hello, World!\rPython")

# When you use \r, any characters printed after it will overwrite the characters on the current line from the beginning.


# outputs :

# Text with newline:
# Hello, World!
# This is on a new line.
# Text with form feed:
# Hello, World!
# This is on a new page (form feed).
# Python World!