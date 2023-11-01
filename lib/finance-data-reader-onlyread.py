# pip install FinanceDataReader
import FinanceDataReader as fdr
import json
from datetime import datetime, timedelta
import exchange_calendars as ecals
import psycopg2


def get_stock_list():



    ########################################################################################
    # fdr 종목정보
    print(f"finance-data start")
    df_kospi = fdr.StockListing("KOSPI")[0:1]
    # df_kospi = fdr.StockListing("KOSPI")
    df_kosdaq = fdr.StockListing("KOSDAQ")[0:1]
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
    


    


if (__name__ == '__main__'):
    
    # krx_json_arr = get_stock_list()
    # print(krx_json_arr)
    
    aa = fdr.DataReader('005930,247540', '2023-11-01')
    print(aa)
    
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    print(fdr.DataReader('005930', '2023-11-01'))
    













