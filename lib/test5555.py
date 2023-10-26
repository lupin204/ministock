from pykiwoom.kiwoom import *
from datetime import datetime
import sqlite3


# prev_list = [(952,953,955)]
# cur_list = [()]

prev_list = [(951, '000', '048410'), (952, '000', '065450'), (953, '000', '161890'), (954, '000', '218150'), (955, '001', '054050'), (956, '001', '066570')]
cur_list = [
    ('20231026', '0815', '000', '돈맥', '048410', '048410', '048410'), #951
    ('20231026', '0815', '000', '돈맥', '218150', '218150', '218150'), #954
    ('20231026', '0815', '001', '돈맥', '066570', '066570', '066570'), #956
    ('20231026', '0815', '001', '돈맥', '123456', '123456', '123456'),
]
update_list = prev_list[:]
insert_list = cur_list[:]
i=0
j=0
for current in cur_list:
    for prev in prev_list:
        print(i, j)
        print('대상' , prev, current)
        if (prev[1] == current[2] and prev[2] == current[4]):
            print('겹친다' , prev, current, len(update_list), len(prev_list), len(insert_list), len(cur_list))
            update_list.remove(prev)
            insert_list.remove(current)
        j = j + 1
    i = i + 1
    j = 0
print('=========================================')
print(prev_list)
print(update_list)
print(cur_list)
print(insert_list)