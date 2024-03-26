

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import csv



options = webdriver.ChromeOptions()
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
options.add_argument('ignore-certificate-errors')
options.add_argument('user-agent=' + user_agent)
options.add_argument("lang=ko_KR")
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("--no-sandbox")

# 사람처럼 보이게 하는 옵션들
options.add_argument("disable-gpu")   # 가속 사용 x
options.add_argument("lang=ko_KR")    # 가짜 플러그인 탑재
options.add_argument('user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36')  # user-agent 이름 설정

# 드라이버 위치 경로 입력
service = Service(ChromeDriverManager().install())
# service = Service("D:/myprjs/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)


#브라우저 꺼짐 방지
# chrome_options.add_experimental_option("detach", True)

#불필요한 에러 메시지 없애기 
options.add_experimental_option("excludeSwitched", ["enable-logging"])



# 웹페이지 해당 주소 이동 
driver.implicitly_wait(5) # 웹 페이지가 로딩될때까지 5초 기다림
driver.maximize_window() # 브라우저 최대화



# 텍스트 파일 경로
txt_file_path = 'sample.txt'

# 텍스트 파일에서 데이터 읽기
loaded_data = {}
with open(txt_file_path, 'r') as txt_file:
    for line in txt_file:
        # 각 줄에서 데이터를 읽어들여 탭을 기준으로 분리합니다.
        market, code, name = line.strip().split('\t')
        # 딕셔너리로 변환하여 loaded_data 리스트에 추가합니다.
        loaded_data[name] = {"market": market, "code": code, "name": name}


theme_arr = []

for idx in range(900, 1000):
    print(f"========================{idx}=================================================")
    
    # https://stockplus.com/m/investing_strategies/topics/771
    driver.get(f"https://stockplus.com/m/investing_strategies/topics/{idx}")
        
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 문서 끝까지 스크롤

    sleep(2) # 웹 페이지가 로딩될때까지 5초 기다림
        
    # 토픽 맥신(MXene)
    text_topic = driver.find_element(By.CSS_SELECTOR, 'main div.topicTop h3 a').text.strip()
    
    if (text_topic != '토픽'):

        topic = text_topic[3:]
        print(f"[{idx}]{topic}")
         
        content_bodys = driver.find_elements(By.CSS_SELECTOR, 'main div.contW01 div.topicTable tbody')

        for content in content_bodys:
            text1 = content.find_element(By.CSS_SELECTOR, 'td.lAlign').text

            try:
                row = [idx, topic]
                row.append(loaded_data[text1]['market'])
                row.append(loaded_data[text1]['code'])
                row.append(text1)
                theme_arr.append(row)
            except:
                print(f'{text1} is not found.')

        
               




print(theme_arr)
sorted_theme_arr = sorted(theme_arr, key=lambda x: (x[0], x[1], x[3]))

#####################################################################################
# CSV 파일 경로
csv_file_path = 'stockplus_theme_list_900.csv'

# CSV 파일 쓰기
with open(csv_file_path, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for row in sorted_theme_arr:
        writer.writerow(row)

print(f'CSV 파일이 {csv_file_path} 경로에 성공적으로 작성되었습니다.')

# 텍스트 파일 경로
txt_file_path = 'stockplus_theme_list_900.txt'

# 텍스트 파일 쓰기
with open(txt_file_path, 'w') as txt_file:
    for row in sorted_theme_arr:
        # 각 요소를 문자열로 변환하여 탭 문자로 연결하여 파일에 씁니다.
        txt_file.write('\t'.join(map(str, row)) + '\n')

print(f'텍스트 파일이 {txt_file_path} 경로에 성공적으로 작성되었습니다.')



