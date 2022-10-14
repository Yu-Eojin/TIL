# 환율을 불러와 변환하는 기능(환전 패키지 사용)
from currency_converter import CurrencyConverter
# 환율정보를 가져온다.
cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')
# 화폐종류 출력
print(cc.currencies)
# 환전 1USD -> 1KRW
print(cc.convert(1,'USD','KRW'))
# ---------------------------------------------------------------------------------

# 사이트에 접속해서 환율정보를 가져오는 방법
import requests
# beautifulsoup : 웹크롤링 패키지. 자매품 selenium
from bs4 import BeautifulSoup

def get_exchange_rate(target1, target2):
    headers = {
        # 웹사이트에 접근할때 웹브라우저인 척하기 위한 브라우저 설정
        'User-Agent': 'Mozilla/5.0',
        'Content-type': 'text/html; charset=utf-8'
    }

    response = requests.get('https://kr.investing.com/currencies/{}-{}'.format(target1,target2), headers=headers)

    content = BeautifulSoup(response.content,'html.parser')
    containers = content.find('span',{'data-test':'instrument-price-last'})

    print(containers.text)

get_exchange_rate('usd','krw')

