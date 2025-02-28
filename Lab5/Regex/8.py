import re

def split_upper(s):
    return re.split(r'(?=[A-Z])', s)

print(split_upper("HelloWorld"))         
print(split_upper("RandomWords"))    
print(split_upper("CounterStrike"))   

