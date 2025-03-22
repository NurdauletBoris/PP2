import re

pattern = r'^a.*b$'

test_strings = [
    "ab",       
    "acdaadadadb",      
    "abc",      

]

for txt in test_strings:
    if re.match(pattern, txt):
        print(f"'{txt}' — Matches")
    else:
        print(f"'{txt}' — Does not match")
