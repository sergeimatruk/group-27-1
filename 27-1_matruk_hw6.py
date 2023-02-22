import re

def get_names(lines):
    names = []
    for line in lines:
        name, surname, *_ = line.split()
        names.append(f'{name} {surname}')
    return names

def get_emails(lines):
    emails = []
    for line in lines:
        line_split = line.split()
        email, *_ = line_split[1:]
        emails.append(email)
    return emails

def get_filenames(lines):
    filenames = []
    for line in lines:
        line_split = line.split()
        email, *_ = line_split[1:]
        filenames.append(filename)
    return filenames

def get_colors(lines):
    colors = []
    for line in lines:
        *_, color = line.split()
        colors.append(color)
    return colors

def write_data_to_file(filename, data):
    with open(filename, 'w') as f:
        f.write('\n'.join(data))

with open('MOCK_DATA.txt', 'r') as f:
    lines = f.readlines()

while True:
    print('Меню:')
    print('1 - Считать имена и фамилии')
    print('2 - Считать все емайлы')
    print('3 - Считать названия файлов')
    print('4 - Считать цвета')
    print('5 - Выход')

    choice = input('Выберите опцию: ')

    if choice == '1':
        names = get_names(lines)
        write_data_to_file('names.txt', names)
    elif choice == '2':
        emails = get_emails(lines)
        write_data_to_file('emails.txt', emails)
    elif choice == '3':
        filenames = get_filenames(lines)
        write_data_to_file('filenames.txt', filenames)
    elif choice == '4':
        colors = get_colors(lines)
        write_data_to_file('colors.txt', colors)
    elif choice == '5':
        break
    else:
        print('Выберите другое значение.')
