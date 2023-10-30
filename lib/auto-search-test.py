from pykiwoom.kiwoom import *
from datetime import datetime
import sqlite3
import FinanceDataReader as fdr
import json
import math


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

# 주식계좌
accounts = kiwoom.GetLoginInfo("ACCNO")
stock_account = accounts[0]

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
for current in cur_list:
    for prev in prev_list:
        if (prev[1] == current[2] and prev[2] == current[4]):
            print('겹친다' , prev, current)
            update_list.remove(prev)
            insert_list.remove(current)

print('=========================================')
print(update_list)
print(insert_list)

# for prev in update_list:
#     cur.execute("UPDATE auto_search SET end_time = ? WHERE id = ?", (base_hm, prev[0]))
# conn.commit()   

# insert #######################################
# cur.executemany(
#     'INSERT INTO auto_search (base_ymd, start_time, formula_id, formula_name, stock_code, stock_name, market) \
#     SELECT ?, ?, ?, ?, ?, (SELECT name FROM stocks WHERE code = ?), (SELECT market FROM stocks WHERE code = ?)', insert_list)
# conn.commit()

conn.close()

print(f"auto-search end")



########################################################################################
# fdr 종목정보
print(f"finance-data start")
# df_kospi = fdr.StockListing("KOSPI")[0:10]
df_kospi = fdr.StockListing("KOSPI")
df_kosdaq = fdr.StockListing("KOSDAQ")
print(f"finance-data end")

# columns, index, records, values, split
kospi_json_str = df_kospi.to_json(orient='records', indent=0, force_ascii=False)
kosdaq_json_str = df_kosdaq.to_json(orient='records', indent=0, force_ascii=False)

kospi_json_arr = json.loads(kospi_json_str)
kosdaq_json_arr = json.loads(kosdaq_json_str)
krx_json_arr = kospi_json_arr + kosdaq_json_arr

krx_dict = {item['Code']: item for item in krx_json_arr}


# 매수는 최대 40만원 1주가 40만원 초과면 1주 매수
max_money_per_stock = 400000

for elem in insert_list:
    new_ticker = elem[4]
    if new_ticker in krx_dict:
        ticker_info = krx_dict[new_ticker]
        
        print(krx_dict[new_ticker])
        
        # 양봉 9% 미만이면 시장가 매수
        if (ticker_info['ChagesRatio'] < 9):
            buy_volume = math.ceil(max_money_per_stock / int(ticker_info['Close']))
            # 삼성전자, 10주, 시장가주문 매수
            kiwoom.SendOrder("시장가매수", "0101", stock_account, 1, ticker_info["Code"], buy_volume, 0, "03", "")
        
        # 양봉 9% 이상이면 오른가격의 절반 가격으로 지정가주문("03") 매수 (10% 오르면 5%가격으로 지정가 주문)
        else:
            buy_price = int(ticker_info['Close']) - math.ceil(int(ticker_info['Changes']) / 2)
            buy_volume = math.ceil(max_money_per_stock / buy_price)
            # 삼성전자, 10주, 지정가주문("00") 매수
            kiwoom.SendOrder("지정가매수", "0101", stock_account, 1, ticker_info["Code"], buy_volume, buy_price, "00", "")
            
            


