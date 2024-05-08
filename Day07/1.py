import random

outFp = None
outStr = ""
fileName = ""

for i in range(0, 10):
    fileName = "ex_"+ str(i) +".txt"
    outFp = open(fileName, "w")
    outFp.writelines("다음의 문제를 제출하세요.\n")
    outFp.writelines("이름 :     학번 : \n")

    for _ in range(0, 10):
        x = str(random.randint(1, 99))
        y = str(random.randint(1, 99))
        operate = random.choice(['+', '-', '*', '/'])
        outFp.writelines(x + " " + operate + " " + y + " = \n")

    outFp.close()