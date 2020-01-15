aa  = [85, 100, 90, 70, 95, 90]

#1. 리스트의 갯수 출력
print("1. 리스트의 갯수 출력")
print(len(aa))

#2. 리스트의 데이터를 바꾸지 않으면서 정렬해서 출력
print("2. 리스트의 출력")
print(sorted(aa))

#3. 90 데이터의 위치를 출력
print("3. 90데이터의 위치 출력")
print(aa.index(90))
print(aa.index(90, 3, 6))
print(aa.index(90, -1))

#4. 마지막 데이터를 꺼내면서 제거해보세요.
print("4. 마지막 데이터를 꺼내고 제거")
print("현재 데이터 : ", aa)
print("마지막 데이터 : ", aa.pop())
print("남아있는 데이터 : ", aa[0:])

#5. bb라는 리스트에 동일한 데이터를 가지도록 처리해보세요
print("5. bb에 동일한 데이터 넣기")
bb = aa.copy()
print(bb)

#6. aa 리스트에서 값이 100인 데이터를 지운다.
print("6. aa 리스트에서 100을 지우기")
aa.remove(100)
print(aa)

#7. aa 리스트의 전체 내용을 지운다.
print("7. aa 리스트의 전체 내용을 지운다")
aa.clear()
print(aa)
