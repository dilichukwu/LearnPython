from collections import defaultdict

shapes_area = defaultdict(lambda : 'Not Applicable')
shapes_area['square'] = 'l x l'
shapes_area['rectangle'] = 'l x b'
shapes_area['circle'] = 'pi x r x r'
shapes_area['pentagon']

print('Nonsense:',shapes_area['nonsense'])
print(shapes_area)
