# set : 중복된 데이터 배제 { v, v, ... }

mySet1 = {1, 2, 3, 4, 5, 4, 5, 3, 6}
print(mySet1, type(mySet1))

# list -> set -> list
mySet2 = ['삼각김밥','바나나','도시락','붕어빵','호떡',
          '삼각김밥','군고구마','바나나','도시락']
print(mySet2)
print(set(mySet2))

# 판매된 상품과 수량을 출력하시오. 중복이 되면 안된다.
print("삼각김밥 : ", mySet2.count("삼각김밥"))

mySet3 = list(set(mySet2))
for menu in mySet3:
    print(menu +"의 갯수 : ", mySet2.count(menu))

mySet1 = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7}
#교집합, 합집합, 차집합, 대칭차집합
print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet1 ^ mySet2)

# 1~100까지의 데이터로 list를 만들어보세요
list1 = []
for i in range(1, 6):
    list1.append(i)

print(list1)

# 컴프리헨션으로 리스트 만들기
list2 = [num for num in range(1, 6)]
print(list2)

#1~10 사이의 3의 배수로 리스트 만들기

list3 = [num for num in range(1, 11) if num%3==0]
print(list3)

# 1~5 사이의 데이터를 제곱 구해서 리스트 만들기
list4 = [num**2 for num in range(1, 6)]
print(list4)

#zip() : 두 리스트를 튜플이나 딕셔너리로 짝지을 때
foods = ["떡볶이","짜장면","라면","피자"]
sides = ["오뎅", "단무지", "김치"]

for f, s in zip(foods, sides):
    print(f, '---->', s)

for f in foods:
    if foods.index(f) > len(sides)-1:
        break
    print(f, '---->', sides[foods.index(f)])

#zip 함수를 이용해서 튜플 리스트, 딕셔너리 만들기
tuplList = list(zip(foods, sides))
print(tuplList)
dic = dict(zip(foods, sides))
print(dic)