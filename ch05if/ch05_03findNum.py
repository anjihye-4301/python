import random

# 랜덤으로 발생된 숫자 10개를 저장하는 리스트
numbers = []
# range(시작번호, 끝번호+1)
for num in range(0, 10):
    print(num)
    # random.randrage(발생시작 숫자, 발생 끝 숫자+1)
    numbers.append(random.randrange(0, 10))

print("생성된 리트스 : ", numbers)

# 0 ~ 9 사이의 각각의 데이터가 있는지 확인해보자

for num in range(0, 10):
    if num in numbers:
        print("숫자 %d는(은) 리스트에 있습니다." % num)
    if num not in numbers:
        print("숫자 %d는(은) 리스트에 없습니다." % num)
