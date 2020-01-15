food={"떡볶이": ["오뎅","순대"],
      "피자": "피클",
      "치킨": "콜라",
      "라면": ["김치","김밥"],
      "짜장면": ["단무지","탕수육"],
      "삼겹살": "상추",
      "맥주": "땅콩"}

while(True):
    myfood = input(str(list(food.keys()))+"중 좋아하는 음식은? ")
    if myfood in food:
        print("%s 궁합 음식은 %s 입니다." %(myfood, food.get(myfood)))
    elif myfood == "":
        break
    else:
        print("해당 음식이 없습니다. 확인해보세요.")