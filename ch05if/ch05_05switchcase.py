def sf1():
    print("첫번째")

def sf2():
    print("두번째")

def sf3():
    print("세번째")

# 함수 매칭(실행 NO)
# json 구조...????
def switch(key):
    return {"1": sf1, "2": sf2, "3": sf3}.get(key, '잘못된 선택')

result = switch("1")
print(result)
# print(result())
result()
switch("2")()
print(switch("4"))