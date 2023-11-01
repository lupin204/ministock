import psycopg2

conn = psycopg2.connect(
    host='arjuna.db.elephantsql.com',
    dbname='fziardgc',
    user='fziardgc',
    password='IjiuOJhm1mxFW_gnVOwlhbbbJKfhO_rU',
    port=5432
)

cur = conn.cursor()



def create_table():
    print('START create table')
    

    # ['Code': '005930', 'ISU_CD': 'KR7005930003', 'Name': '삼성전자', 'Market': 'KOSPI', 'Dept': '', 'Close': '67100', 
    # 'ChangeCode': '2', 'Changes': -1100, 'ChagesRatio': -1.61, 'Open': 67100, 'High': 67400, 'Low': 66900, 'Volume': 7032462, 
    # 'Amount': 471934306900, 'Marcap': 400572409105000, 'Stocks': 5969782550, 'MarketId': 'STK'}, ... ]
    cur.execute("CREATE TABLE IF NOT EXISTS stocks \
        (base_ymd VARCHAR, code VARCHAR, name VARCHAR, market VARCHAR, volume INT8, amount INT8, \
        change_code VARCHAR, changes INT, ratio VARCHAR, close INTEGER, open INT, high INT, low INT, \
        marcap INT8, stocks INT8, marketid VARCHAR, dept VARCHAR, PRIMARY KEY(base_ymd, code))")
    conn.commit()
    
            
        # Volume 거래량 140000주 
        # Marcap 시가총액  2107 4719 5000
        # ChagesRatio  7.14   7.14%
        # Stocks 상장주식수
        # Amount 거래대금  :387793 319 400
    
    
    # ("001", "돈맥", "돈맥잡기")
    cur.execute("CREATE TABLE IF NOT EXISTS search_formula \
        (formula_id VARCHAR PRIMARY KEY, formula_name VARCHAR, formula_desc VARCHAR)")
    conn.commit()
    
    
    # (1, "231018", "0910", "1100", "001", "돈맥", "005930", "삼성전자", "KOSPI")
    cur.execute("CREATE TABLE IF NOT EXISTS auto_search \
        (id INTEGER NOT NULL DEFAULT nextval('seq_auto_search_id'::regclass) PRIMARY KEY , \
        base_ymd VARCHAR, start_time VARCHAR, end_time VARCHAR, \
        formula_id VARCHAR, formula_name VARCHAR, stock_code VARCHAR, stock_name VARCHAR, market VARCHAR)")
    conn.commit()
    
    
    # (1, "231018", "0910", "1500", "001", "돈맥", "005930", "삼성전자", "KOSPI", 12000, 30, 360000)
    cur.execute("CREATE TABLE IF NOT EXISTS buy_sell_history \
        (id INTEGER NOT NULL DEFAULT nextval('seq_buy_sell_history_id'::regclass) PRIMARY KEY , \
        base_ymd VARCHAR, buy_time VARCHAR, sell_time VARCHAR, \
        formula_id VARCHAR, formula_name VARCHAR, stock_code VARCHAR, stock_name VARCHAR, market VARCHAR, \
        price INT, volume INT, amount INT )")
    conn.commit()
    
    cur.close()
    conn.close()
    print('END create table')
    
    
def create_sequence():
    
    cur.execute("CREATE SEQUENCE seq_auto_search_id \
    INCREMENT 1 \
    START 1 \
    MINVALUE 1 \
    MAXVALUE 9223372036854775807 \
    CACHE 1")
    conn.commit()
    
    cur.execute("CREATE SEQUENCE seq_buy_sell_history_id \
    INCREMENT 1 \
    START 1 \
    MINVALUE 1 \
    MAXVALUE 9223372036854775807 \
    CACHE 1")
    conn.commit()

def truncate_table():
    cur.execute("TRUNCATE")



# database data type (파이썬 = SQLite)
# None=NULL, int=INTEGER, float=REAL, str=TEXT, bytes=BLOB
if (__name__ == '__main__') :
    # truncate_table()
    # create_sequence()
    create_table()

    
