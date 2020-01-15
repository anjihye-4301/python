# 함수 선언
def my_func():
    print('함수를 호출')

# 전역변수 선언
g_var = 100

# 메인 코드
if __name__=='__main__':
    print('메인 함수 부분 실행')
    my_func()
    print('전역 변수 값 : ',g_var)

'''
def main():
    print('메인 함수 부분 실행')
    my_func()
    print('전역 변수 값 : ',g_var)

after 1:
if __name__ == '__main__':
    main()
after 2:
main()

    # main()만 선언한 경우는 시작부분으로 인정하지 않는다.
    # 함수 선언(def) 없이 처리문을 만들거나 if__name__ 선언해서 main을 선언한다.
'''
# _ 을 사용하는 경우
'''
1. 인터프리터에서 마지막 값을 저장하고 싶을 때
2. 값을 무시하고 싶을 때
3. 변수나 함수명에 특별한 의미를 부여하고 싶을 때
4. 숫자 리터럴 값의 자릿수 구분을 위한 구분자로 사용할 때
'''