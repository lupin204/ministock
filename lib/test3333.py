from pykiwoom.kiwoom import *
from datetime import datetime
import sqlite3


# db
conn = sqlite3.connect('d:/myprjs/ministock/lib/ministock.db')
cur = conn.cursor()

# base
base_ymd = datetime.today().strftime('%Y%m%d')
base_hm = datetime.today().strftime('%H%M')



# insert #######################################
cur.execute(
    'INSERT INTO search_formula (formula_id, formula_name, formula_desc) VALUES (?, ?, ?)', (base_ymd+base_hm+'test3333', base_hm, 'test3333'))
conn.commit()

conn.close()


