from pykiwoom.kiwoom import *
import pprint

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
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)
    
    
condition_index = conditions[1][0]
condition_name = conditions[1][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(condition_index, condition_name)
print(codes)
for ticker in codes:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)
    

condition_index = conditions[2][0]
condition_name = conditions[2][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(condition_index, condition_name)
print(codes)
for ticker in codes:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)
    
    
condition_index = conditions[3][0]
condition_name = conditions[3][1]
codes = kiwoom.SendCondition("0101", condition_name, condition_index, 0)

print(condition_index, condition_name)
print(codes)
for ticker in codes:
    name = kiwoom.GetMasterCodeName(ticker)
    print(ticker, name)
    
    
import telegram
import asyncio
from telegram.ext import Updater
from telegram.ext import MessageHandler, filters

from datetime import datetime


TOKEN = '6363791280:AAEkRY1l6OyB_DrGKOvmSZ6EBkW2SU56SBk'
ChatId = '6578669349'

current_time = datetime.now().strftime("%H:%M:%S")
msg = f'[{current_time}] hello'

bot = telegram.Bot(token=TOKEN)

asyncio.run(bot.sendMessage(chat_id=ChatId , text=msg))
    
    
# updater 
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def get_dividiend(code):
    dividend = f"{code} = {condition_name}"
    return dividend

# message handler
def echo(update, context):
    user_id = update.effective_chat.id
    user_text = update.message.text
    dividend = get_dividiend(user_text)
    text = f"배당수익률: {dividend}"
    context.bot.send_message(chat_id=user_id, text=text)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# polling
updater.start_polling()

