import re

"""
\t  - Lowercase t. Matches tab.
\n  - Lowercase n. Matches newline.
\r  - Lowercase r. Matches return.
\A  - Uppercase a. Matches only at the start of the string. Works across multiple lines as well.
\Z  - Uppercase z. Matches only at the end of the string.
"""

print("\\t (TAB) example: ", re.search(r'Eat\tcake', 'Eat	cake').group())