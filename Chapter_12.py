import unicodedata

# 12.1 Create a Unicode string called mystery and assign it the value '\U0001f984'.
# Print mystery and its Unicode name.

print("12.1--------------------------------------------------------------------------------------")
mystery = '\U0001F984'
print(mystery)
print(unicodedata.name(mystery))

print("12.2--------------------------------------------------------------------------------------")
# 12.2 Encode mystery, this time using UTF-8, into the bytes variable pop_bytes. Print pop_bytes.
pop_bytes = mystery.encode("UTF-8")
print(pop_bytes)

print("12.3--------------------------------------------------------------------------------------")
# 12.3 Using UTF-8, decode pop_bytes into the string variable pop_string. Print pop_string.
# Is pop_string equal to mystery?
pop_string = pop_bytes.decode("UTF-8")
print(pop_string)

print("12.4--------------------------------------------------------------------------------------")
# 12.4 When you’re working with text, regular expressions come in very handy.
# We’ll apply them in a number of ways to our featured text sample.
# It’s a poem titled “Ode on the Mammoth Cheese,” written by James McIntyre in 1866 in homage to
# a seven-thousand-pound cheese that was crafted in Ontario and sent on an international tour.
# If you’d rather not type all of it, use your favorite search engine and cut and paste the words
# into your Python program, or just grab it from Project Gutenberg.
# Call the text string mammoth.
mammoth_file = open(file="mammoth.txt", mode="r")
mammoth = mammoth_file.read()
print(mammoth)

print("12.5--------------------------------------------------------------------------------------")
# 12.5 Import the re module to use Python’s regular expression functions.
# Use the re.findall() to print all the words that begin with c.
import re

regex = re.compile('\\bc\\w*')
g = regex.findall(mammoth)
print(g)

print("12.6--------------------------------------------------------------------------------------")
# 12.6 Find all four-letter words that begin with c.
g = re.findall(r'\bc\w{3}\b', mammoth)
print(g)

print("12.7--------------------------------------------------------------------------------------")
# 12.7 Find all the words that end with r.
g = re.findall('\\w*r\\b', mammoth)
print(g)

print("12.8--------------------------------------------------------------------------------------")
# 12.8 Find all words that contain exactly three vowels in a row.
g = re.findall(r'\w*[aeiou]{3}\w*', mammoth)
print(g)

print("12.9--------------------------------------------------------------------------------------")
# 12.9 Use unhexlify to convert this hex string (combined from two strings to fit on a page)
# to a bytes variable called gif:
# '47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'
from binascii import unhexlify, hexlify

gif = unhexlify('47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b')
print(gif)
print(bytes.fromhex('47494638396101000100800000000000ffffff21f90401000000002c000000000100010000020144003b'))
print(gif.hex())
print(hexlify(gif))


print("12.10--------------------------------------------------------------------------------------")
# 12.10 The bytes in gif define a one-pixel transparent GIF file, one of the most common
# graphics file formats. A legal GIF starts with the ASCII characters GIF89a. Does gif match this?
print(gif.startswith(b'GIF89a'))
print(re.match(b'GIF89a', gif).group())

print("12.11--------------------------------------------------------------------------------------")
# 12.11 The pixel width of a GIF is a 16-bit little-endian integer beginning at byte offset 6,and the
# height is the same size, starting at offset 8. Extract and print these values for gif. Are they both 1?
import struct

width, height = struct.unpack('<HH', gif[6:10])
print(width, height)