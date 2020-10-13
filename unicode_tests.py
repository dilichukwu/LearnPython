import html.entities

print(html.unescape("caf&eacute;"))
print(html.unescape("&#233;"))
print(html.entities.codepoint2name[ord('\u00e9')])
print(ord('\u00e9'))
print("caf\u005f".encode("ascii"))

for ch in range(255):
    print(chr(ch))