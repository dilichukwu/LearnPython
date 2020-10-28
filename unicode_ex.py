import unicodedata
from html.entities import codepoint2name

for i in range(256):
    print(chr(i))

print("\U0000ffff")
print("\u00ff")
print("\N{LATIN CAPITAL LETTER A WITH ACUTE}")

print(unicodedata.lookup("LATIN CAPITAL LETTER E WITH ACUTE"))
print(unicodedata.name("\u00EF"))
print(unicodedata.name("$"))

print(ord('A'))