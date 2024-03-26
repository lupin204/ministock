import pandas as pd
from pykrx import stock
from pykrx import bond
from time import sleep

from datetime import datetime
import os
import time

import csv

# CSV 파일에 쓸 데이터
data = []

market_list = ['KOSPI', 'KOSDAQ']


for market_nm in market_list:
    ticker_list = stock.get_market_ticker_list(market=market_nm)
    for tickers in ticker_list:
        corp_name = stock.get_market_ticker_name(tickers)

        row = [market_nm, tickers, corp_name]
        data.append(row)

############################################################################
# CSV 파일 경로
csv_file_path = 'sample.csv'

# CSV 파일 쓰기
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in data:
        writer.writerow(row)

print(f'CSV 파일이 {csv_file_path} 경로에 성공적으로 작성되었습니다.')

# 텍스트 파일 경로
txt_file_path = 'sample.txt'

# 텍스트 파일 쓰기
with open(txt_file_path, 'w') as txt_file:
    for row in data:
        # 각 요소를 문자열로 변환하여 탭 문자로 연결하여 파일에 씁니다.
        txt_file.write('\t'.join(map(str, row)) + '\n')

print(f'텍스트 파일이 {txt_file_path} 경로에 성공적으로 작성되었습니다.')