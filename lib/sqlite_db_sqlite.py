import sqlite3
import sys

conn = sqlite3.connect('d:/myprjs/ministock/lib/ministock.db')

cur = conn.cursor()



def create_table():
    print('START create table')
    

    # ['Code': '005930', 'ISU_CD': 'KR7005930003', 'Name': '삼성전자', 'Market': 'KOSPI', 'Dept': '', 'Close': '67100', 
    # 'ChangeCode': '2', 'Changes': -1100, 'ChagesRatio': -1.61, 'Open': 67100, 'High': 67400, 'Low': 66900, 'Volume': 7032462, 
    # 'Amount': 471934306900, 'Marcap': 400572409105000, 'Stocks': 5969782550, 'MarketId': 'STK'}, ... ]
    conn.execute("CREATE TABLE IF NOT EXISTS stocks \
        (base_ymd TEXT, code TEXT, name TEXT, market TEXT, volume INTEGER, amount INTEGER, \
        change_code TEXT, changes INTEGER, ratio TEXT, close INTEGER, open INTEGER, high INTEGER, low INTEGER, \
        marcap INTEGER, stocks INTEGER, marketid TEXT, dept TEXT, PRIMARY KEY(base_ymd, code))")
    
    
            
        # Volume 거래량 140000주 
        # Marcap 시가총액  2107 4719 5000
        # ChagesRatio  7.14   7.14%
        # Stocks 상장주식수
        # Amount 거래대금  :387793 319 400
    
    
    # ("001", "돈맥", "돈맥잡기")
    conn.execute("CREATE TABLE IF NOT EXISTS search_formula \
        (formula_id TEXT PRIMARY KEY, formula_name TEXT, formula_desc TEXT)")
    
    
    # (1, "231018", "0910", "1100", "001", "돈맥", "005930", "삼성전자", "KOSPI")
    conn.execute("CREATE TABLE IF NOT EXISTS auto_search \
        (id INTEGER PRIMARY KEY AUTOINCREMENT, base_ymd TEXT, start_time TEXT, end_time TEXT, \
        formula_id TEXT, formula_name TEXT, stock_code TEXT, stock_name TEXT, market TEXT)")
    
    
    
    print('END create table')
    

def truncate_table():
    conn.execute("TRUNCATE")



# database data type (파이썬 = SQLite)
# None=NULL, int=INTEGER, float=REAL, str=TEXT, bytes=BLOB
if (__name__ == '__main__') :
    # truncate_table()
    create_table()
    
