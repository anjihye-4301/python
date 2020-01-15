#print('\u2605')

start, star = 0, 1

for i in range(1, 10):
    start = (11 - star) // 2
    for j in range(1, start):
        print('\u3000', end='')
    for j in range(1, star+1):
        print('\u2605', end='')
#    for j in range(1, start):
#        print('  ', end='')
    print("")
    if i<=4:
        star += 2
    if i>4:
        star -= 2


print('------')

totalRow = 9
inc = 1
# blankcnt -. 4, 3, 2, 1, 0, 1, 2, 3, 4
# totalRow //2 -> 4 ==> range(1, totalRow // 2 + 1)
blankcnt, starcnt, multi = 4, 1, 1
for i in range(1, totalRow+1):
    # 빈 공간 출력
    blankcnt = (totalRow // 2 - i + 1) * multi
    for j in range(1, blankcnt+1):
        print("  ", end="")
    # 별 출력
    for k in range(1, starcnt+1):
        print("\u2605", end="")
    print()
    starcnt += 2 * multi
    # 별을 최대치 출력하면 공백은 증가(+값)해야 하고 별의 갯수 감소(-)
    if i== totalRow // 2 :
        multi *= -1
