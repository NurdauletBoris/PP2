import re

text = "BINGO BANGO BONGO BISH BASH BOSH."

result = re.sub(r'[ ,.]', ':', text)

print(result)
