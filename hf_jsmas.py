import requests
from urllib import parse
from bs4 import BeautifulSoup as bs
import pandas as pd



# beatifulsoup이란?
# xml, html로 부터 원하는 데이터를 가져오도록 비슷한 분류의 데이터별로 나누어주는(parsing) 파이썬 라이브러리


#전라남도 천연기념물 명소
url = 'http://apis.data.go.kr/6460000/jnMonument/getNdtrMonumentList'
key = 'Kl2M0LhJOX1kHS4lHm0PxPIYKDOF0Ob1KNNZ2%2FbQOHjaOIQeyzD4LWXgjOL0MxVClcVwNYiBUoV8iqOcoGAfYA%3D%3D'


params ={
         'serviceKey' : parse.unquote(key),
         'tourNm' : '갓바위',
         'pageSize' : '10',
         'startPage' : '0'
         }

response = requests.get(url, params=params)
soup = bs(response.text, features="xml") # xml분류방식으로 비슷한 분류 데이터를 데이터별로 나누는 parsing

items = soup.find_all('list') # list태그 안에있는 데이터만 가져오기 <list> 데이터 </list>

lst = []
for item in items:
    l = {}
    for arg in item:
        l[arg.name] = arg.text
    lst.append(l)

title = {'tourAddr' : '주소',
         'tourId': '고유코드',
         'tourMainImg': '메인이미지경로',
         'tourMenuNm': '메뉴명',
         'tourNm': '명칭',
         'tourTel': '전화번호',
         'tourXpos': '경도',
         'tourYpos': '위도',
         'tourZoneCd': '지역코드',
         'tourZoneNm': '지역명'
}


df = pd.DataFrame(lst) #dataframe형태로 변환
df.columns = df.columns.map(title)
print(df)



# 보증한도 조회
# url = 'http://apis.data.go.kr/B551408/hg-guarntee-limit-amt/guarntee-info'
# key = 'Kl2M0LhJOX1kHS4lHm0PxPIYKDOF0Ob1KNNZ2%2FbQOHjaOIQeyzD4LWXgjOL0MxVClcVwNYiBUoV8iqOcoGAfYA%3D%3D'
# params ={'serviceKey' : '',
#          'reqLoanAmt' : '200000000',
#          'repayMthdDvcd' : '01',    # 상환방식 , 01: 일시상환 02: 원금균등상환 03: 원금불균등상환 04: 원리금균등상환 05: 체증식상환 06: 혼합형상환
#          'guarntRamt' : '0',        # 기보증잔액
#          'incmAmt' : '30000000',    # 연소득
#          'debtAmt' : '10000000',    # 부채금액
#          'rentGuarntAmt' : '400000000', # 목적물 임차보증금액
#          'glPrimeYn' : 'N',             # 보증한도우대가구 해당여부
#          'glexceptYn' : 'N',            # 채권보전조치 선택 여부
#          'numOfRows' : '10',            # 한 페이지 결과 수
#          'pageNo' : '1',                # 페이지 번호
#          'dataType' : 'XML' }           # 데이터타입



#주택연금예상연금 조회 서비스
# url= 'http://apis.data.go.kr/B551408/rg-mon-pmt-amt/pmt-info'
# params ={'serviceKey' : 'GWUu7X1riqWPpfpDSyv9gkSbiUipnX4ciPh9cl38uOPUbEN42SQbb3AeNrDXvJx2xCdjoaYSZ%2FraMdqqIee0zg%3D%3D',
#          'pageNo' : '1',
#          'numOfRows' : '10',
#          'housePrc' : '250000000',
#          'houseDvcd' : '01',
#          'pnsnPayMthdDvcd' : '01',
#          'mmPayAmtIndcDvcd' : '01',
#          'joinPersBrthDy' : '19510205',
#          'sposBrthDy' : '19540605',
#          'payTermCd' : '01',
#          'wdrwLmtSetpAmt' : '1000000',
#          'dataType' : 'XML'
#          }
#
# response = requests.get(url, params=params)
# print(response.content)