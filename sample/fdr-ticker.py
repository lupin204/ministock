# pip install FinanceDataReader
import FinanceDataReader as fdr
import json
from datetime import datetime, timedelta
import exchange_calendars as ecals
import sqlite3


# df = fdr.DataReader('094360,002720', '2023-10-30')
# df.head(10)
# print(df.head(10))


# df = fdr.DataReader('094360,002720', '2023-10-30')
# print(df)



# df1 = fdr.DataReader('094360,002720,024060', '2023-10-30')
# print(df1)


########################################################################################
# fdr 종목정보
print(f"finance-data start")
df_kospi = fdr.StockListing("KOSPI")[0:10]
# df_kospi = fdr.StockListing("KOSPI")
# df_kosdaq = fdr.StockListing("KOSDAQ")
print(f"finance-data end")

# columns, index, records, values, split
kospi_json_str = df_kospi.to_json(orient='records', indent=0, force_ascii=False)
# kosdaq_json_str = df_kosdaq.to_json(orient='records', indent=0, force_ascii=False)

kospi_json_arr = json.loads(kospi_json_str)
arr_dict = {item['Code']: item for item in kospi_json_arr}
print(arr_dict)

find_ticker = "111111"
if find_ticker in arr_dict:
    print("yes")
    print(arr_dict[find_ticker])
else:
    print("nono")
# kosdaq_json_arr = json.loads(kosdaq_json_str)


# [{'Code': '308700', 'ISU_CD': 'KR7308700004', 'Name': '테크엔', 'Market': 'KONEX', 'Dept': '일반기업부', 'Close': '265', 
# 'ChangeCode': '4', 'Changes': 34, 'ChagesRatio': 14.72, 'Open': 265, 'High': 265, 'Low': 201, 'Volume': 2251, 'Amount': 596451, 
# 'Marcap': 1060000000, 'Stocks': 4000000, 'MarketId': 'KNX'}, ... ]

# ChangeCode:{'0':'거래정지', '1':'양봉', '2':'음봉', '3':'그대로', '4':'상한가', '5':'하한가'}
# krx_json_arr = kospi_json_arr + kosdaq_json_arr
# print(krx_json_arr)

