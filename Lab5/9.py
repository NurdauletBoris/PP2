import re

def add_spaces(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

print(add_spaces("HelloWorld"))         
print(add_spaces("PenPineApple"))   
print(add_spaces("InsertSpacesHere"))   

