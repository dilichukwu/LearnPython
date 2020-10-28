def counter_inf(start, step):
    while True:
        yield start
        start += step

for i in counter_inf(0,1):
    print(i)
    