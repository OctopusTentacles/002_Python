# 9.5 Перемещение курсора в файле. Метод seek

import os

path = os.getcwd()

speakers_file = open(os.path.join(path,'Part2_Modul09\speakers.txt'), 'r', encoding='utf-8')
data = speakers_file.read(12)
data2 = speakers_file.read(8)
# read(20) перемещает курсор по файлу, 

print(data)
print(data2)


speakers_file.seek(1)
data2 = speakers_file.read(5)
# seek ставит курсор на позицию, НО в файле должна быть
# латиница, с кириллицей будет ощибка

print(data2)

speakers_file.close()