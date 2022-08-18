import os.path

with open('1.txt', encoding='utf-8') as file1:
    f1 = file1.readlines()
    f1_name = os.path.basename('1.txt')
    res_f1 = [f'{f1_name}\n', f'{str(len(f1))}\n']
    res_f1.extend(f1)
    res_f1.append('\n')


with open('2.txt', encoding='utf-8') as file2:
    f2 = file2.readlines()
    f2_name = os.path.basename('2.txt')
    res_f2 = [f'{f2_name}\n', f'{str(len(f2))}\n']
    res_f2.extend(f2)
    res_f2.append('\n')

with open('3.txt', encoding='utf-8') as file3:
    f3 = file3.readlines()
    f3_name = os.path.basename('3.txt')
    res_f3 = [f'{f3_name}\n', f'{str(len(f3))}\n']
    res_f3.extend(f3)
    res_f3.append('\n')

def add_info(file):
    with open('res.txt', 'a', encoding='utf-8') as res:
        res.writelines(file)
    return

file_list = [res_f1, res_f2, res_f3]
file_list.sort(key=len)
for add_file in file_list:
    add_info(add_file)

