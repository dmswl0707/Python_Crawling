## 네이버 API 방법 1 (urllib.request)

import os
import sys
import urllib.request

# 네이버 API 불러오기

client_id = '----------'
client_secret= '-------------'

#keyword 입력
encText = urllib.parse.quote('와인')
url = "https://openapi.naver.com/v1/search/blog?query=" + encText # json 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # xml 결과

#리퀘스트 받아오기
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

#디코드하여 출력
if (rescode==200):
    response_body = response.read()
    decode = response_body.decode('utf-8')
    print(decode)
#else:
    #print("Error Code:" + rescode)


import json
import pandas as pd

#디코드한 내용 json파일로 변환
jsonArray = json.loads(decode)
result = jsonArray.get('items')
print(result)

#파일 써서 json을 csv로 변환
file = open('../data_file/items.json', 'w+')
file.write(json.dumps(result))

df = pd.read_json('../data_file/items.json')
df.to_csv('crawling_naver_blog.csv',encoding='utf-8-sig',index=False)