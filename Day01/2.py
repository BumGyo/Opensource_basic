ginsu = int(input("입력 진수 결정(16/10/8/2) : "))
num = input("값 입력 : ")
if (ginsu == 16):
    num = int(num, 16)
elif (ginsu == 10):
    num = int(num)
elif (ginsu == 8) :
    num = int(num, 8)
elif (ginsu == 2) :
    num = int(num, 2)

print("16진수 ==> ", hex(num))
print("10진수 ==> ", num)
print("8진수  ==> ", oct(num))
print("2진수  ==> ", bin(num))