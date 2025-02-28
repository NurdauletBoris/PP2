import re

pattern = r'^ab*$'
test_strings = ["a", "ab", "abb", "abbb", "b", "aa", "abc", "aabb", ""]

for txt in test_strings:
    if re.match(pattern, txt):
        print(f"'{txt}' — Match")
    else:
        print(f"'{txt}' — Doesn't")
