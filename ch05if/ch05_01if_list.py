fruit = ['사과','배','딸기','포도']
print(fruit)
fruit.append('귤')
print(fruit)

search = input("과일 이름을 입력하세요 : ")

if search in fruit :
    print(search,"가 있습니다.")
else:
    print(search,"가 없습니다.")