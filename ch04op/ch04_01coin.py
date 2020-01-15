def change(a, money):
    print(a, "원짜리 ==>", money//a, "개")
    # money = money - (a * (money//a))
    money = money % a
    return money


money = int(input("교환할 돈은 얼마? "))
print("\n")
a = 500
money = change(a, money)
a = 100
money = change(a, money)
a = 50
money = change(a, money)
a = 10
money = change(a, money)
print("바꾸지 못한 잔돈 ==>", money,"원")