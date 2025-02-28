import re

pattern = r'^ab{2,3}$'

test_strings = ["abb", "abbb", "ab", "abbbb", "a", "b", "aab", "abbbc", "abbc"]

for txt in test_strings:
    if re.match(pattern, txt):
        print(f"'{txt}' — Match")
    else:
        print(f"'{txt}' — Doesn't match")
