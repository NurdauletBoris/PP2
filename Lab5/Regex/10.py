import re

def to_snake(camel):
    return re.sub(r'([A-Z])', r'_\1', camel).lower().lstrip('_')

print(to_snake("HelloWorld"))         
print(to_snake("ZaWarudo"))   
print(to_snake("MineCraft"))     
