# 1~10까지 출력
'''
i = 1
while i<11:
    print(i)
    i+=1
'''
# 1부터 숫자를 계속 더해서 더한 숫자가 100보다 커지면 빠져나가서 출력
i=1
sum=0
while sum<=100:
    sum += i
    i += 1
print("1부터 %d까지의 합은 %d입니다." %(i, sum))

i=1
sum=0
while True:
    sum += i
    i += 1
    if sum>100 :
        break
print("1부터 %d까지의 합은 %d입니다." %(i, sum))

# 1~10 출력 홀수만 출력
# 1부터 시작하면서 2씩 증가 -> 1번째 방법
# 짝수인 경우 출력하지 않고 반복처리를 계속 할 수 있도록 한다. -> 2번째 방법(continue)
print("-------------")
i=1
while i<11:
    if i%2 == 1 :
        print(i)
    i += 1
print("-------------")
i = 1
while i < 11:
    print(i)
    i += 2
print("-------------")
i=0
while True:
    i += 1
    if i > 10 :
        break
    if i % 2 == 0 :
        continue
    print(i)
