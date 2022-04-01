import pandas as pd
import random

first_names_csv = pd.read_csv('./assets/firstnames_datasheet.csv')
first_names_arr = first_names_csv['name'].to_list()

first_names_boys = first_names_csv[first_names_csv['sex'] == 'boy']['name'].to_list()
first_names_girls = first_names_csv[first_names_csv['sex'] == 'girl']['name'].to_list()
mix_names = first_names_boys + first_names_girls

last_names_csv = pd.read_csv('./assets/surnames_datasheet.csv')
last_names_arr = last_names_csv['name'].str.title().to_list()

number_of_iterations = int(input("How many names do you need? (Def: 10) ") or '10')
sex_of_names = str(input("What type of names would you like? boys / girls / mixed (Def: mixed) ") or 'mixed').lower()
names_output = str(input("How would you like the names? dict / list / strings (Def: dict) ") or 'dict').lower()

if sex_of_names == 'girls':
    use_names = first_names_girls
elif sex_of_names == 'boys':
    use_names = first_names_boys
else:
    random.shuffle(mix_names)
    use_names = mix_names

if names_output == 'strings':
    generated_names = ''
else:
    generated_names = []

for item in range(number_of_iterations):
    random.shuffle(use_names)
    random.shuffle(last_names_arr)
    
    new_first_name = use_names[random.randint(0, len(use_names) - 1)]
    new_last_name = last_names_arr[random.randint(0, len(last_names_arr) - 1)]

    if names_output == 'strings':
        generated_names += f'{new_first_name} {new_last_name}\n'
    elif names_output == 'list':

        generated_names.append(f'{new_first_name} {new_last_name}')
    else:
        generated_names.append({
            'first_name': new_first_name,
            'last_name': new_last_name
        })

print(generated_names)
