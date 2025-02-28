import re

pattern = r'^[A-Z][a-z]+$'

test_strings = [
    "Hello",   
    "hello",    
    "WORLD",    

]

for txt in test_strings:
    if re.match(pattern, txt):
        print(f"'{txt}' — Matches")
    else:
        print(f"'{txt}' — Does not match")