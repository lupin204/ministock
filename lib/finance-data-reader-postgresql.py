# pip install FinanceDataReader
import FinanceDataReader as fdr
import json
from datetime import datetime, timedelta
import exchange_calendars as ecals
import psycopg2


def get_stock_list():
    ########################################################################################
    # yyyy-mm-dd
    today = datetime.today().strftime('%Y-%m-%d')
    # 어제 days = 1
    # today = (datetime.today() - timedelta(days = 1)).strftime('%Y-%m-%d')

    # 오늘은 개장일인지 확인
    print(f"exchange_calendars start")
    is_today_session = ecals.get_calendar("XKRX").is_session(today)
    print(f"exchange_calendars end")


    ########################################################################################
    # fdr 종목정보
    print(f"finance-data start")
    #df_kospi = fdr.StockListing("KOSPI")[0:10]
    df_kospi = fdr.StockListing("KOSPI")
    df_kosdaq = fdr.StockListing("KOSDAQ")
    print(f"finance-data end")

    # columns, index, records, values, split
    kospi_json_str = df_kospi.to_json(orient='records', indent=0, force_ascii=False)
    kosdaq_json_str = df_kosdaq.to_json(orient='records', indent=0, force_ascii=False)

    kospi_json_arr = json.loads(kospi_json_str)
    kosdaq_json_arr = json.loads(kosdaq_json_str)
    print(kospi_json_str)

    # [{'Code': '308700', 'ISU_CD': 'KR7308700004', 'Name': '테크엔', 'Market': 'KONEX', 'Dept': '일반기업부', 'Close': '265', 
    # 'ChangeCode': '4', 'Changes': 34, 'ChagesRatio': 14.72, 'Open': 265, 'High': 265, 'Low': 201, 'Volume': 2251, 'Amount': 596451, 
    # 'Marcap': 1060000000, 'Stocks': 4000000, 'MarketId': 'KNX'}, ... ]
    
    # ChangeCode:{'0':'거래정지', '1':'양봉', '2':'음봉', '3':'그대로', '4':'상한가', '5':'하한가'}
    krx_json_arr = kospi_json_arr + kosdaq_json_arr
    
    #     1일 거래량 2천억
    # 10초 거래량 10억
    # 1분 거래량 50억
    
    return krx_json_arr
    



def insert_stock_to_db(krx_json_arr):

    conn = psycopg2.connect(
        host='arjuna.db.elephantsql.com',
        dbname='fziardgc',
        user='fziardgc',
        password='IjiuOJhm1mxFW_gnVOwlhbbbJKfhO_rU',
        port=5432
    )
    
    cur = conn.cursor()

    today_ymd = datetime.today().strftime('%Y%m%d')
    stocksList = []
    for elem in krx_json_arr:
        print(elem)
        stocksList.append((today_ymd, elem['Code'], elem['Name'], elem['Market'], elem['Volume'], elem['Amount'], 
                            elem['ChangeCode'], elem['Changes'], elem['ChagesRatio'], elem['Close'], elem['Open'], elem['High'], elem['Low'], 
                            elem['Marcap'], elem['Stocks'], elem['MarketId'], elem['Dept'], ))
    
    
    print('=========================================')
    
    # delete #######################################
    cur.execute('DELETE FROM stocks')
    conn.commit()
    
    # insert #######################################
    print('postgresql insert start')
    
    args = ','.join(cur.mogrify("(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", i).decode("utf-8")
                    for i in stocksList)
    cur.execute("INSERT INTO stocks VALUES " + (args))
    
    
    # cur.executemany(
    # 'INSERT INTO stocks VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', stocksList)
    conn.commit()
    print('postrgresql insert end')
    
    cur.close()
    conn.close()
    
    


if (__name__ == '__main__'):
    
    krx_json_arr = get_stock_list()
    print(krx_json_arr)
    
    insert_stock_to_db(krx_json_arr)












