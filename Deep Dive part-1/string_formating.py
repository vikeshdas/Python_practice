import string
formatter = string.Formatter()

# The string.Formatter class in Python is used for creating and customizing string formatting. It provides several methods to facilitate string formatting operations

#                   format(format_string, *args, **kwargs)
result = formatter.format("Hello, {}!", "world")
print(result)  # output Hello, world!


# ********************************************************************
# This method is similar to format(), but instead of accepting *args and **kwargs, it accepts a tuple args and a dictionary kwargs

# passing in tuple
result = formatter.vformat("Hello, {} {}!", ("vikesh","das"), {})
print(result)

# passing in dictionary
result = formatter.vformat("Hello, {first} {last}!", ("vikesh","das"), {"first":"vikesh","last":"das"})
print(result)


# ******************************************************************
# parse(format_string):
# This method parses the given format_string and returns an iterable of tuples representing the string format. Each tuple consists of four elements: (literal_text, field_name, format_spec, conversion).

for literal_text, field_name, format_spec, conversion in formatter.parse('Hello, {name}!'):
    print('literal_text:', literal_text)
    print('field_name:', field_name)
    print('format_spec:', format_spec)
    print('conversion:', conversion)

# ******************************************************************
# get_field(field_name, args, kwargs):
# This method is used internally by vformat() to get the value of a field

formatter = string.Formatter()
value = formatter.get_field('name', (), {'name': 'world'})
print(value)  # output: world



