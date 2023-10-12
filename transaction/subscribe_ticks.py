import time
import pythoncom
import win32com.client



#실시간 호가를 수신할 종목의 종목코드.
#반드시 크레온/싸이보스에서 사용하는 종목코드를 넣을 것. 'A123456', 'Q567890', ...
CODES = ( 'A005930',       #삼성전자
          'A000660',       #하이닉스
          'A068270',       #셀트리온
          )



class TickerHandler:
    '''이벤트 핸들러. 대신증권 서버에서 새로운 호가를 받았을 때 실행할 동작 설정.
    '''
    def set_param(self, inst):
        self.inst = inst


    #호가를 수신하면 self.OnRecieved( )가 실행됨. 종목코드와 매도/매수호가를 튜플로 저장함.
    def OnReceived(self):
        buff = (  self.inst.GetHeaderValue(0),     #종목코드
                  self.inst.GetHeaderValue(7),     #매도호가
                  self.inst.GetHeaderValue(8),     #매수호가
                  )

        #수신한 호가 정보를 화면에 표시함.
        print('code: {}, ask: {:8,}, bid: {:8,}'.format(*buff))



#여러개의 이벤트 핸들러를 저장할 빈 리스트 만들기.
tickers = [ ]
#하나의 종목코드당 하나의 이벤트핸들러를 설정한다.
for code in CODES:
    #크레온/싸이보스의 실시간 호가 담당 모듈인 'StockCur'를 불러오고
    #'StockCur'에서 이벤트가 발생하면 'class.TickerHandler.OnRecieved( )'를 실행하도록 둘을 연결한다.
    ticker = win32com.client.DispatchWithEvents('dscbo1.StockCur', TickerHandler)
    #'class.TickerHandler.OnReceived( )'에서 새로운 틱 데이터를 읽어올 수 있도록 'dscbo1.StockCur.GetHeaderValue(i)'를 지정한다.
    ticker.set_param(ticker)
    #실시간 호가를 수신할 대상의 종목코드를 입력한다.
    ticker.SetInputValue(0, code)
    #실시간 호가수신을 시작한다.
    ticker.Subscribe( )
    #이벤트핸들러를 리스트에 저장한다.
    tickers.append(ticker)


try:
    while True:
        #1초간 쉰다. CPU 사용률 100% 방지.
        time.sleep(1)
        #이벤트가 있었는지 확인한다. 있다면 연결된 이벤트핸들러를 실행한다.
        pythoncom.PumpWaitingMessages( )
#ctrl+C 종료시 
except:
    #모든 이벤트핸들러의
    for ticker in tickers:
        #실시간 호가 수신을 중지한다.
        ticker.Unsubscribe( )
    print('exit')

