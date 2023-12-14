class MyDerivedDict(dict):
    def __init__(self, *args, **kwargs):
        super(MyDerivedDict, self).__init__(*args, **kwargs)

my_dict = MyDerivedDict({'a': 1, 'b': 2, 'c': 3})

print(my_dict)
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict['d'] = 4

print(my_dict)