from pykiwoom.kiwoom import *
import pprint

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

####################################################################################
# 종목코드 전체
# "0" 코스피 "10" 코스닥 "8" ETF
kospi = kiwoom.GetCodeListByMarket('0')
kosdaq = kiwoom.GetCodeListByMarket('10')
etf = kiwoom.GetCodeListByMarket('8')

print(len(kospi), kospi)
print(len(kosdaq), kosdaq)
print(len(etf), etf)


####################################################################################
# 단일 종목명
name = kiwoom.GetMasterCodeName("005930")
print(name)



####################################################################################
# 연결상태 확인
state = kiwoom.GetConnectState()
if state == 0:
    print("미연결")
elif state == 1:
    print("연결완료")
    
    
####################################################################################
# 상장주식수 얻기 >> Integer.maxValue = 2147483647
stock_cnt = kiwoom.GetMasterListedStockCnt("005930")
print("삼성전자 상장주식수: ", stock_cnt)


####################################################################################
# 감리구분 >>  '정상', '투자주의', '투자경고', '투자위험', '투자주의환기종목'
감리구분 = kiwoom.GetMasterConstruction("005930")
print(감리구분)




####################################################################################
# 상장일 
상장일 = kiwoom.GetMasterListedStockDate("005930")
print(상장일)
print(type(상장일))        # datetime.datetime 객체


####################################################################################
# 전일가
전일가 = kiwoom.GetMasterLastPrice("005930")
print(int(전일가))
print(type(전일가))


####################################################################################
# 종목상태  >>  ['증거금20%', '담보대출', '신용가능']
종목상태 = kiwoom.GetMasterStockState("005930")
print(종목상태)


####################################################################################
# 테마

tickers = kiwoom.GetThemeGroupCode('330') #화장품
for ticker in tickers:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)

# group = kiwoom.GetThemeGroupList(1)
# pprint.pprint(group)


