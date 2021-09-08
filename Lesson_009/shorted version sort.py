some_dict = {'a': 5, 'n': 3, 'z': 9}

print(type(sorted([(v, k) for (k, v) in some_dict.items()], reverse=True)))
