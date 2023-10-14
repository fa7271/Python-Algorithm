import sys

sys.stdin = open('/Users/song/Desktop/Python/Python/h.txt', 'r')

money = int(input())
MachineDuck = list(map(int,input().split()))

def jun(money):
    jun = 0
    for x in MachineDuck:
        if money >= x:
            if money == 0:
                break
            jun = money // x
            money = money % x
    return money + jun * MachineDuck[-1]
def sung(money):
    stock = 0
    for x in range(len(MachineDuck) - 3):
        # 주식이 있고 3일 상승장 판매
        if stock != 0 and MachineDuck[x] < MachineDuck[x+1] < MachineDuck[x+2] :
            money = stock * MachineDuck[x+3]
            stock = 0
        # 구매 하락장  구매
        if  MachineDuck[x] > MachineDuck[x+1] > MachineDuck[x+2] :
            stock += money // MachineDuck[x+3]
            if money != 0:
                money = money % MachineDuck[x+3]
    # 남은돈
    return money + stock * MachineDuck[-1]
X = jun(money)
Y = sung(money)
print("BNP" if X > Y else ("TIMING" if X < Y else "SAMESAME"))

