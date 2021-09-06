import re

"""
{x}  - Repeat exactly x number of times.
{x,}  - Repeat at least x times or more.
{x, y}  - Repeat at least x times but no more than y times. 
"""

print(re.search(r'\d{9,10}', '0987654321').group())