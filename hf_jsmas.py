import requests


url = 'http://apis.data.go.kr/B551408/hg-guarntee-limit-amt/guarntee-info'
params ={'serviceKey' : 'GWUu7X1riqWPpfpDSyv9gkSbiUipnX4ciPh9cl38uOPUbEN42SQbb3AeNrDXvJx2xCdjoaYSZ%2FraMdqqIee0zg%3D%3D',
         'reqLoanAmt' : '200000000',
         'repayMthdDvcd' : '01',    # 상환방식 , 01: 일시상환 02: 원금균등상환 03: 원금불균등상환 04: 원리금균등상환 05: 체증식상환 06: 혼합형상환
         'guarntRamt' : '0',        # 기보증잔액
         'incmAmt' : '30000000',    # 연소득
         'debtAmt' : '10000000',    # 부채금액
         'rentGuarntAmt' : '400000000', # 목적물 임차보증금액
         'glPrimeYn' : 'N',             # 보증한도우대가구 해당여부
         'glexceptYn' : 'N',            # 채권보전조치 선택 여부
         'numOfRows' : '10',            # 한 페이지 결과 수
         'pageNo' : '1',                # 페이지 번호
         'dataType' : 'XML' }           # 데이터타입

response = requests.get(url, params=params)
print(response.content)


# 주택연금예상연금 조회 서비스
# url = 'http://apis.data.go.kr/B551408/rg-mon-pmt-amt/pmt-info'
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