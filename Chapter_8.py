print("\n8.1----------------------------------------------------------------------------------------")
# 8.1 Make an English-to-French dictionary called e2f and print it.
# Here are your starter words: dog is chien, cat is chat, and walrus is morse.
e2f = dict(dog='chien', cat='chat', walrus='morse', horse='cheval', cow='vache')

for e, f in e2f.items():
    print(e, ':', f)

print("\n8.2----------------------------------------------------------------------------------------")
# 8.2 Using your three-word dictionary e2f, print the French word for walrus.
print(e2f['walrus'])

print("\n8.3----------------------------------------------------------------------------------------")
# 8.3 Make a French-to-English dictionary called f2e from e2f. Use the items method.
f2e = {}
for e, f in e2f.items():
    f2e[f] = e

print(f2e)

print("\n8.4----------------------------------------------------------------------------------------")
# 8.4 Print the English equivalent of the French word chien.
print(f2e['chien'])

print("\n8.5----------------------------------------------------------------------------------------")
# 8.5 Print the set of English words from e2f.
es = set(e2f)
print(es)

print("\n8.6----------------------------------------------------------------------------------------")
# 8.6 Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants',
# and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'.
# Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'.
# Make all the other keys refer to empty dictionaries.

life = {}
life = \
    {'animals':
        {'cats': ['Henri', 'Grumpy', 'Lucy'],
         'octopi': [],
         'emus': []
        },
     'plants': {},
     'other': {}
    }


print("\n8.7----------------------------------------------------------------------------------------")
# 8.7 Print the top-level keys of life.
k = list(life)
print(k)
for key in life:
    print(key)


print("\n8.8----------------------------------------------------------------------------------------")
# 8.8 Print the keys for life['animals'].
for k in life['animals']:
    print(k)


print("\n8.9----------------------------------------------------------------------------------------")
# 8.9 Print the values for life['animals']['cats'].
for v in life['animals']['cats']:
    print(v)


print("\n8.10----------------------------------------------------------------------------------------")
# 8.10 Use a dictionary comprehension to create the dictionary squares.
# Use range(10) to return the keys, and use the square of each key as its value.
dict_square = {k: k*k for k in range(1, 10)}
print(dict_square)


print("\n8.11----------------------------------------------------------------------------------------")
# 8.11 Use a set comprehension to create the set odd from the odd numbers in range(10).
odd_set = {num for num in range(1, 10) if num % 2 == 1}
print(odd_set)
print(type(odd_set))

print("\n8.12----------------------------------------------------------------------------------------")
# 8.12 Use a generator comprehension to return the string 'Got ' and a number for the numbers in range(10).
# Iterate through this by using a for loop.
got_num = ('Got ' + str(num) for num in range(10))
print(got_num)
print(next(got_num))
print(next(got_num))


print("\n8.13----------------------------------------------------------------------------------------")
# 8.13 Use zip() to make a dictionary from the key tuple ('optimist', 'pessimist', 'troll') and the
# values tuple ('The glass is half full', 'The glass is half empty', 'How did you get a glass?').
dic = dict(zip(('optimist', 'pessimist', 'troll'),
               ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')))
print(dic)


print("\n8.14----------------------------------------------------------------------------------------")
# 8.14 Use zip() to make a dictionary called movies that pairs these lists: titles = ['Creature of Habit',
# 'Crewel Fate', 'Sharks On a Plane'] and plots = ['A nun turns into a monster', 'A haunted yarn shop',
# 'Check your exits']
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
movies = dict(zip(titles, plots))
print(movies)