import random

def lotto():
    print("** 로또 추첨을 시작합니다. **\n")
    num = []
    for _ in range(6):
        num.append(random.randrange(1, 45))
    print("추첨된 로또 번호 ==>", *num)
    
lotto()