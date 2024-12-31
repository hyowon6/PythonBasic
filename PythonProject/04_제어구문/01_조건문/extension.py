filenames = ['intra.h', 'intra.c', 'input.txt', 'run.py']

results = []
for name in filenames:
    extension = name.split('.')[-1]
    if extension == 'h' or extension =='c':
        results.append(name)

print(results)