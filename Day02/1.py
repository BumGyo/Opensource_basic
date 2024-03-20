## 변수 선언 부분 ##
select, answer, numStr, num1, num2 = 0, 0, "", 0, 0

## 메인 코드 부분 ##
select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

if select == 1 :
    numStr = input(" *** 수식을 입력하세요 : ")
    print(" ", numStr, "결과는 ", eval(numStr), "입니다.")

elif select == 2:
    num1 = int(input(" *** 첫 번째 숫자를 입력하세요 : "))
    num2 = int(input(" *** 두 번째 숫자를 입력하세요 : "))

    ## 반복문을 이용해 합계 구하기 ##
    for i in range(num1, num2 + 1):
        answer += i

    print("%d + ... + %d는 %d입니다." %(num1, num2, answer))