ddd = dict()
names = ['dean', 'olusha', 'anna', 'ivan', 'anna', 'dina', 'olusha']
for name in names:
    ddd[name] = ddd.get(name, 0) + 1
print(ddd)
