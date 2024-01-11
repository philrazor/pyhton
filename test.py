names = {'philip':'+254-748-065-379' , 
         'eva':'+254-113-197-587' , 
         'francis':'+254-724-329-919'
         }

numbers = []

name_to_search = input('enter name to search number for: ')

lower_name = name_to_search.lower()
for name in names:
    per_name = names[name]
    numbers.append(per_name)

if lower_name in names:
    print(f'the number for {lower_name} is {names[lower_name]}')
else:
    print("name not found")    


number_to_add = input('enter number to add: ')
name_to_add = input('enter number to name: ')

def add_name_number(number,name):
    added_number = number
    added_name  = name

    new_names  = {
        added_name : added_number
    }
    final_names = names + new_names
    def print_new_dictionary(final_names):
        for name in final_names:
            name = final_names[name]
            print(f'the updated dictionary: {name}')
    print_new_dictionary(final_names)
    return final_names


add_name_number(number_to_add,name_to_add)
