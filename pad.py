from collections import Counter

string = "OESSEOOEREOEESO#ETTTOEERSTTRETT#T"

for key, value in Counter(string).items():
    print(key, value)

print(len(string))
