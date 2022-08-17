import os.path

with open('1.txt', encoding='utf-8') as file1:
    f1 = file1.readlines()
    f1_name = os.path.basename('1.txt')

with open('2.txt', encoding='utf-8') as file2:
    f2 = file2.readlines()
    f2_name = os.path.basename('2.txt')

with open('3.txt', encoding='utf-8') as file3:
    f3 = file3.readlines()
    f3_name = os.path.basename('3.txt')

with open('res.txt', 'w', encoding='utf-8') as res:
    res.write(f1_name + '\n')
    res.write(str(len(f1)) + '\n')
    res.writelines(f1)


#print(f1_name)