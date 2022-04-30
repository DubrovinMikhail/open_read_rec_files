FILE_NAME = 'recipes.txt'


def cook_book(name_file: str):
    with open(name_file, 'r', encoding='utf-8') as file:
        cook_list = []
        recipt = []
        for line in file:
            if line != '\n':
                recipt.append(line.strip())
            else:
                cook_list.append(recipt)
                recipt = []
    cook_book_list = []
    for recipe in cook_list:
        recip_dict = {}
        recip_name = recipe.pop(0)
        recip_dict[recip_name] = []
        for i in range(int(recipe.pop(0))):
            recip_dict[recip_name].append(
                {'ingredient_name': recipe[i].split('|')[0].strip(),
                 'quantity': recipe[i].split('|')[1].strip(),
                 'measure': recipe[i].split('|')[2].strip()})
        cook_book_list.append(recip_dict)
    return cook_book_list


# for recip in cook_book(FILE_NAME):
#     for key, value in recip.items():
#         print(f'{key}:')
#         for ingredient in value:
#             print(ingredient)


def get_shop_list_by_dishes(dishes, person_count):
    dishes_shop_dict = {}
    for dish in dishes:
        for page in cook_book(FILE_NAME):
            if dish in page.keys():
                for ingredient in page[dish]:
                    ingredient_name = ingredient['ingredient_name']
                    if ingredient_name in dishes_shop_dict.keys():
                        quantity = dishes_shop_dict[ingredient_name]['quantity'] + int(ingredient['quantity']) * person_count
                    else:
                        quantity = int(ingredient['quantity']) * person_count
                    dishes_shop_dict[ingredient_name] = {'measure': ingredient['measure'], 'quantity': quantity}
    return dishes_shop_dict


shop_list = get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 2)

# for key, value in shop_list.items():
#     print(f'{key}: {value}')

FILE_ONE = '1.txt'
FILE_TWO = '2.txt'
FILE_THREE = '3.txt'
MERGE_FILE = 'log.txt'

def file_merge(file_1: str, file_2: str, file_3: str, merge_file):
    file_list = [file_1, file_2, file_3]
    file_list_data = []
    for file in file_list:
        file_dict = {'file_name': file, 'count_row': 0, 'data': ''}
        with open(file, 'r', encoding='utf-8') as file_data:
            for row in file_data:
                file_dict['count_row'] += 1
                file_dict['data'] += row
            file_list_data.append(file_dict)
            file_list_data_sort = sorted(file_list_data, key=lambda d : d['count_row'])
    with open(merge_file, 'w') as file_text:
        for row_text in file_list_data_sort:
            file_text.write(f'{row_text["file_name"]}\n')
            file_text.write(f'{row_text["count_row"]}\n')
            file_text.write(f'{row_text["data"]}\n')


file_merge(FILE_ONE, FILE_TWO, FILE_THREE,MERGE_FILE)



# with open('1.txt','r',  encoding='utf-8') as ferq:
#     print(ferq.read())