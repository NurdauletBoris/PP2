import re

pattern = r'^[a-z]+_[a-z]+$'

test_strings = [
    "hello_world",  
    "hello_world_again",  
    "hello_World",  
    "hello123_world",  
    "helloworld",  

]

for txt in test_strings:
    if re.match(pattern, txt):
        print(f"'{txt}' — Matches")
    else:
        print(f"'{txt}' — Does not match")
