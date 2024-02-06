# from pykiwoom.kiwoom import *
#
# kiwoom = Kiwoom()
# kiwoom.CommConnect(block=True)
#
# # 주식계좌
# accounts = kiwoom.GetLoginInfo("ACCNO")
# stock_account = accounts[0]
#
# # 삼성전자, 10주, 시장가주문 매수
# kiwoom.SendOrder("시장가매수", "0101", "8069450011", 1, "005930", 10, 0, "03", "")
# print('=== 매수접수완료 ===')
#
#


from pykiwoom.kiwoom import *

kiwoom = Kiwoom()
kiwoom.CommConnect(block=True)

print(kiwoom.GetConnectState())

# df = kiwoom.block_request("opw00004",
#                           계좌번호="8069450011",
#                           비밀번호="0000",
#                           output="종목별계좌평가현황",
#                           next=0)
# print(kiwoom.GetCommRealData("005930",10))
kiwoom.CommRqData("현재가","opt10001",0,"0001")
kiwoom.OnReceiveTrData("0001","현재가","opt10001","주식기본정보요청",0)
test = kiwoom.GetCommData("opt10001","주식기본정보",0,"현재가")
print(test)
# print(df.T)/
