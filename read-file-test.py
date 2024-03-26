# 텍스트 파일 경로
txt_file_path = 'sample.txt'

# 텍스트 파일에서 데이터 읽기
loaded_data = []
with open(txt_file_path, 'r') as txt_file:
    for line in txt_file:
        # 각 줄에서 데이터를 읽어들여 탭을 기준으로 분리합니다.
        market, code, name = line.strip().split('\t')
        # 딕셔너리로 변환하여 loaded_data 리스트에 추가합니다.
        loaded_data.append({"market": market, "code": code, "name": name})

# 읽어들인 데이터 출력
print(loaded_data)