# 크레온으로 작성된 코드를 키움증권에서 사용할 수 있도록 리팩토링
# 계좌번호 : 8069-4500 11
from pykiwoom.kiwoom import *
from datetime import datetime

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

def dbgout(message):
    '''인자로  받은 문자열을 파이썬 셸과 슬랙에 동시출력'''
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message)

def printlog(message, *args):
    """인자로 받은 문자열을 파이썬 셸에 출력한다."""
    print(datetime.now().strftime('[%m/%d %H:%M:%S]'), message, *args)

def get_current_price(code):
    '''인자로 받은 종목의 현재가, 매도호가, 매수호가를 반환'''
