from random import randint

# ID Generator
print('*** ID Generator System ***')
name = input('What is your name?: ')
surename = input('What is your surename?: ')
year = input('What is your year of birth: ')

name_sub_string = name[0:2].upper()
surename_sub_string = surename[0:2].upper()
year_sub_string = year[2:]
random_number = randint(1000, 9999)

print(f'Hi {name} cityzen of Gotham City')
print('\tYour new ID is:')
print(f'\t{name_sub_string}{surename_sub_string}{year_sub_string}{random_number}')