"""
Take two tuples and create a dictionary with elements from one tuple as
 keys and elements from the other tuple as values.

"""

keys_tuple = ('apple', 'banana', 'cherry')

values_tuple = (1, 2, 3)

result_dict = dict(zip(keys_tuple, values_tuple))
print(result_dict)
