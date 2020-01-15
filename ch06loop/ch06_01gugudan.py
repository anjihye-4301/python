# for i in range(1, 10):
#     print(i, end='')

num1, num2, answer = 0, 0, 0

num1 = int(input("시작할 단수 입력 : "))
num2 = int(input("마지막 단수 입력 : "))

for num in range(1, 10):
    for dan in range(num1, num2+1):
        answer = dan * num
        print("%d x %d = %2d" %(dan, num, answer), end=' ')
    print("")
