aa = [10, 20, 30, 40, 50]
# list aa의 값의 순서를 거꾸로 정렬하여 출력하시오
# aa = aa[::-1]
aa.reverse()
print(aa)

# 일부 데이터의 변경
# aa 리스트 데이터 중 세번째 30을 300으로
aa[2] = 300
print(aa)

# 첫번째 50 -> 500, 두번째 40 -> 400으로 변경
aa[0:2] = [500, 400]
print(aa)

# aa 리스트의 두번째 세번째 데이터를 하나로 합침
aa[1:3] = [700]
print(aa)

# aa 리스트 안에 리스트가 들어간다.
aa[1] = [1000, 2000]
print(aa)
print(aa[0], type(aa[0]))
print(aa[1], type(aa[1]))

# aa 리스트 데이터 삭제
aa[2:] = []
print(aa)