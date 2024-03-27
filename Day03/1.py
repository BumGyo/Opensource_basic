food = {'떡볶이':'오뎅', '짜장면':'단무지', '라면':'김치', '피자':'', '맥주':'', '치킨':'', '삼겹살':''}

while True : 
    print(list(food.keys()), "중 좋아하는 음식은? ", end = ' ')
    suki = input();
    if suki in food :
        print('<' + str(suki) + '>' + " 궁합 음식은 " + '<' + str(food.get(suki)) + '>' + "입니다.")
    elif suki == '끝':
        break
    else :
        print("그런 음식 없습니다. 확인해 보세요.")