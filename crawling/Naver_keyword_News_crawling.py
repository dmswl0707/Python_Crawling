## 네이버 API 방법 2 (requests)


import requests
import pandas as pd
import re
from pprint import pprint

client_id = '4xDTNJmoO6VnncM8JjYA'
client_secret= '3JwXbDA0ax'

search_word = '스마트오더' #검색어
encode_type = 'json' #출력 방식 json 또는 xml
max_display = 100 #출력 뉴스 수
sort = 'date' #결과값의 정렬기준 시간순 date, 관련도 순 sim
start = 1 # 출력 위치

url = f"https://openapi.naver.com/v1/search/news.{encode_type}?query={search_word}&display={str(int(max_display))}&start={str(int(start))}&sort={sort}"

headers = {
    'X-Naver-client-Id':client_id,
    'X-Naver-client-Secret':client_secret
}

#HTTP요청 보내기
r = requests.get(url, headers=headers)
print(r.headers['content-type'])
r.content.decode('utf-8') #r.encoding = 'utf-8'

#요청 결과 보기 200 이면 정상적으로 요청 완료
print(r)

data = r.json()
#print(data)

df= pd.DataFrame(data['items'])


def clean_html(x):
    x = re.sub("\&\w*\;","",x)
    x = re.sub("<.*?>","",x)
    return x

df['title'] = df['title'].apply(lambda x : clean_html(x))
df['description'] = df['description'].apply(lambda x : clean_html(x))

df.to_csv(f'news_search_result_{search_word}.csv')
