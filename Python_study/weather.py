weather = "맑음" # weather 변수에 값 할당
print("비가 오나요?", weather == "비") 
if weather == "비": # weather의 값이 "비"와 같으면 조건식이 true이므로 만족, 코드를 실행 
    print("우산을 가져간다.")
elif weather == "맑음":
    print("날씨가 좋다.")
else: # 조건식이 False이면 실행
    print("우산을 가져가지 않는다.")
# 조건문이 False 여야만 elif의 결과가 나온다. 