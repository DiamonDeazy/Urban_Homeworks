def print_params(a = 1, b = 'String', c = True):
    print(a, b, c)

# Default parameters
print_params()
print_params(21, 'Message', False)
print_params('Str', 90)
print_params(1.23)
print_params(b = 25)
print_params(c = [1, 2, 3])

# Parameters unpacking
values_list = ['String', True, 13]
values_dict = {'a': 13, 'b': False, 'c': 'Float'}
print_params(*values_list)
print_params(**values_dict)

# Unpacking + individual parameters
values_list_2 = [3.14, 'Number']
print_params(*values_list_2, 42)