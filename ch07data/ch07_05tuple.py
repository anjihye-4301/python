# list는 데이터 변경이 가능 [], tuple은 데이터 변경이 불가능 ()
tt=(10, 20, 30)

print(tt, type(tt))

# tt.append(40)
# tt[2] = 300

print(tt[0:2])

# tt1 = tt.copy()
tt1 = tt
print(tt1)
print(tt1 + tt)
print(tt*3)

# tuple -> (10, 20, 30) --> (10, 200, 30) ??
# tutle -> list -> 데이터 수정 -> tuple

ll = list(tt)
ll[tt.index(20)] = 200
tt = tuple(ll)
print(tt)