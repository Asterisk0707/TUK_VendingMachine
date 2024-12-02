class MenuClass:
    def __init__(goods):
       goods.menu = ['','오아시스', '레몬워터', '옥수수수염차', '콘트라베이스', '트레비', '밀키스', 'pepsi', '핫식스', '칠성사이다', '코코리치', 'Lipton', 'Tropicana', 'Ghana', '레쓰비', '칸타타', '케토레이', '코코포도', '식혜']
       goods.price = [0, 600, 1500, 1300, 2000, 1000, 800, 800, 1000, 1000, 1000, 1000, 600, 600, 1000, 1000 ,800, 800, 800]
       goods.total = 0



    # 메뉴 보이기
    def menu_print(goods):
        i = 1
        while i< len(goods.menu):
            print(i, goods.menu[i], goods.price[i])
            i = i+1
        print("============================== \n")

    # 음료  선택
    def menu_select(goods):
        n = int(input("음료를 선택하세요 : "))
        sum_ = int(input("음료의 개수 선택하세요 : "))
        price_sum = goods.price[n] * sum_
        print(goods.menu[n], goods.price[n],'원 ', '합계 ', price_sum, '원')
        print("============================== \n")

        # 음료 추가

        while n != 0:
            print()
            n = int(input("추가로 주문하시려면 음료 번호를, 가격을 지불하려면 0을 누르세요 : "))
            if n > 0 and n < len(goods.menu):
                sum_ = int(input("음료의 개수 선택하세요 : "))
                price_sum = price_sum + goods.price[n] * sum_
                print(goods.menu[n], goods.price[n],'원 ', '합계 ', price_sum, '원')
                print("============================== \n")
            else :
                if n == 0 :
                    print("============================== \n")
                else :
                    print("없는 음료입니다.")
                    print("============================== \n")
        goods.total += price_sum
        return price_sum

    # 지불
    def menu_pay(goods, total_price):
        # 지불 방법 출력
        n = int(input("카드 결제는 0번을 현금결제는 1번을 입력하세요. "))
        if n == 0:
            print("총", total_price,"원 결제되었습니다.")
            print("선택하신 음료가 나옵니다. ")
            print("============================== \n")
        if n == 1:
            money = int(input("지폐를 투입하세요 : "))
            change = money - total_price
            if change < 0:
                print("돈이 부족합니다. 현금을 반환합니다.")
                print("============================== \n")
            else:
                print("거스름돈", change, "원 을(를) 반환합니다.")
                print("============================== \n")




#인스턴스 생성
menu1 = MenuClass()

while(1):
    print("╭──────────── \n")
    print("╰─➛✎﹏ | welcome ! 한국공학대학교 음료 자판기입니다. \n")
    menu1.menu_print()
    total_price = menu1.menu_select()
    menu1.menu_pay(total_price)
    input("사용해주셔서 감사합니다.")
    break
