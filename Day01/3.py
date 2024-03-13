num = int(input("교환할 돈은 얼마 ? "))

cnt_500 = num // 500
num = num % 500
print("500원 짜리 ==> %d개" %(cnt_500))

cnt_100 = num // 100
num = num % 100
print("100원 짜리 ==> %d개" %(cnt_100))

cnt_50 = num // 50
num = num % 50
print("50원 짜리 ==> %d개" %(cnt_50))

cnt_10 = num // 10
num = num % 10
print("10원 짜리 ==> %d개" %(cnt_10))
print("바꾸지 못한 잔돈 ==> %d원" %num)