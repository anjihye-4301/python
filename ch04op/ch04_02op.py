# 문자열과 숫자는 연산이 되지 않는다.
# print("100" + 1)

# 문자열로 연산되도록 하려면
print("100" + str(1))

# 숫자로 연산
print(int("100") + 1)

print(10 + 1.1)
print(10 + int(1.5))

# 0100
a = 4
print(a << 1)
print(a >> 1)
