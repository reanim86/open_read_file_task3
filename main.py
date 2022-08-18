import os.path

def open_file(file):
    with open(file, encoding='utf-8') as file_open:
        f = file_open.readlines()
        f_name = os.path.basename(file)
        res_f = [f'{f_name}\n', f'{str(len(f))}\n']
        res_f.extend(f)
        res_f.append('\n')
    return res_f

def add_info(file):
    with open('res.txt', 'a', encoding='utf-8') as res:
        res.writelines(file)
    return

file_list = []
base_file = os.listdir('./base_file')

for file in base_file:
    file_list.append(open_file(f'./base_file/{file}'))
file_list.sort(key=len)

for add_file in file_list:
     add_info(add_file)

