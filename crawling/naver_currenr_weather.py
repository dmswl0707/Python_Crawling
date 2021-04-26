from bs4 import BeautifulSoup
from pprint import pprint
import requests

html = requests.get("https://search.naver.com/search.naver?query=날씨") #특정 웹페이지를 요청

pprint(html.text) #딕셔너리가 길 경우, 보기에 편하다

#라이브러리를 불러와 텍스트를 보기 좋게 파싱해준다
soup= BeautifulSoup(html.text, 'html.parser')

# soup의 find 함수르 가져와 data1에 저장
# div 태그와 딕셔너리를 불러온다
data1 = soup.find('div', {'class':'weather_box'})

# 현재 위치 값을 가지고 있는 태그와 딕셔너리를 변수로 생성하고 프린트한다
find_address = data1.find('span', {'class':'btn_select'}).text
print('현재 위치: '+find_address)

# 현재 온 값을 가지고 있는 태그와 딕셔너리를 변수로 생성하고 프린트한다
find_currenttemp = data1.find('span',{'class': 'todaytemp'}).text
print('현재 온도: '+find_currenttemp+'℃')

# find 함수는 첫 정보만을 반환하므로 findAll 함수를 이용
# data2에 저장된 태그와 딕셔너리 값을 인덱스를 사용해 프린트한다
data2 = data1.findAll('dd')
find_dust = data2[0].find('span', {'class':'num'}).text
find_ultra_dust = data2[1].find('span', {'class':'num'}).text
find_ozone = data2[2].find('span', {'class':'num'}).text
print('현재 미세먼지: '+find_dust)
print('현재 초미세먼지: '+find_ultra_dust)
print('현재 오존지수: '+find_ozone)
