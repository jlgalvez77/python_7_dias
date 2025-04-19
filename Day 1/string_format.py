# String formating in Python

var_hello = 'Hello'
var_world = 'World'

# Print values
print(var_hello, var_world)

# String concatenation
var_hello_world = var_hello + ' ' + var_world
print(var_hello_world)

# String interpolation
print(f'{var_hello} {var_world}')

# Multiline interpolation
print(f'''My string:
    {var_hello} 
        {var_world}''')