from pykiwoom.kiwoom import *
from datetime import datetime
import sqlite3


# db
conn = sqlite3.connect('d:/myprjs/ministock/lib/ministock.db')
cur = conn.cursor()

# base
search_tuples = []
base_ymd = datetime.today().strftime('%Y%m%d')
base_hm = datetime.today().strftime('%H%M')

# stocks info
cur.execute('SELECT code, name FROM stocks')
stocks_tuples = cur.fetchall() # (('005930','삼성전자'), ...)
stocks_dicts = dict((x,y) for x, y in stocks_tuples) # {'005930':'삼성전자'}

cur.execute("select id, formula_id, stock_code \
    from auto_search \
    where base_ymd = strftime('%Y%m%d', 'now') \
    and end_time is null")
prev_tuples = cur.fetchall()






# 로그인
kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

# 조건식을 PC로 다운로드
kiwoom.GetConditionLoad()

# 전체 조건식 리스트 얻기
# [('000', '돈맥'), ('001', '불꽃시세'), ('002', '하루홍삼')]
conditions = kiwoom.GetConditionNameList()

# 0번 조건식에 해당하는 종목 리스트 출력
print(conditions)

condition_index = conditions[0][0]
condition_name = conditions[0][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)



print(condition_index, condition_name)
print(codes)
for ticker in codes:
    search_tuples.append((base_ymd, base_hm, condition_index, condition_name, ticker, ticker, ticker))
    print(ticker, stocks_dicts[ticker])
    
    
condition_index = conditions[1][0]
condition_name = conditions[1][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(condition_index, condition_name)
print(codes)
for ticker in codes:
    search_tuples.append((base_ymd, base_hm, condition_index, condition_name, ticker, ticker, ticker))
    print(ticker, stocks_dicts[ticker])
    

condition_index = conditions[2][0]
condition_name = conditions[2][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(condition_index, condition_name)
print(codes)
for ticker in codes:
    search_tuples.append((base_ymd, base_hm, condition_index, condition_name, ticker, ticker, ticker))
    print(ticker, stocks_dicts[ticker])
    
    
condition_index = conditions[3][0]
condition_name = conditions[3][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(condition_index, condition_name)
print(codes)
for ticker in codes:
    search_tuples.append((base_ymd, base_hm, condition_index, condition_name, ticker, ticker, ticker))
    print(ticker, stocks_dicts[ticker])

print('=========================================')
print(search_tuples)
print(prev_tuples)



# id, formula_id, stock_code
prev_list = list(prev_tuples)
# base_ymd, base_hm, condition_index, condition_name, ticker, ticker, ticker
cur_list = list(search_tuples)

update_list = prev_list[:]
insert_list = cur_list[:]
i = 0
j = 0
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

for prev in update_list:
    cur.execute("UPDATE auto_search SET end_time = ? WHERE id = ?", (base_hm, prev[0]))
 
conn.commit()   

# insert #######################################
cur.executemany(
    'INSERT INTO auto_search (base_ymd, start_time, formula_id, formula_name, stock_code, stock_name, market) \
    SELECT ?, ?, ?, ?, ?, (SELECT name FROM stocks WHERE code = ?), (SELECT market FROM stocks WHERE code = ?)', insert_list)
conn.commit()

conn.close()

print(f"auto-search end")

