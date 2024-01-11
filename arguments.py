names = ['philip', 'george', 'mbiu', 'caro', 'eva']


def print_multiple_arg(*names):
    for name in names:
        print(name, end=', ')
    print()


passed_arg = print_multiple_arg(*names)


def check(passed_arg):
    search_name = input('Enter search name: ')
    if search_name in names:
        print(f'Found {search_name}')
    else:
        print(f'{search_name} not found')

    status = {
        names[0]: 'logged in',
        names[1]: 'not logged',
        names[2]: 'not logged',
        names[3]: 'not logged',
        names[4]: 'logged in',
    }

    logged = [name for name, status in status.items() if status == 'logged in']
    not_logged = [name for name, status in status.items() if status == 'not logged']

    print('Logged:', logged)
    print('Not logged:', not_logged)


check(passed_arg)
