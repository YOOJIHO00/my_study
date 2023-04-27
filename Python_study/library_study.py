# 표준 라이브러리
# 모듈을 모아놓은것을 패키지 라고 부른다.
# 파이썬에서 지원하는 표준 라이브러리
# 파이썬을 설치할 때 자동으로 함께 설치된다.
# 따로 설치하지 않고 import 명령으로 불러온다.

# datetime 라이브러리
# 날짜 관련 라이브러리
# datetime의 date객체 사용

# import datetime
# day1 = datetime.date(2023, 4, 17)
# day_end = datetime.date(2023, 9, 18)
# diff = day_end - day1
# print(diff.days)

# 2018년 8월 6일 무슨요일일까요?
# # weekday() --> 0:월요일 ~~ 6: 일요일
# import datetime
# day = datetime.date(2018, 8, 6)
# weekdays = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
# print(day.weekday())   
# print(weekdays[day.weekday()])

# datetime의 포맷팅 코드
# 날짜와 시간을 표시하는 방법
# 년/월/일
# 월/일/년
# 일/월/년
# 2023년 4월 27일
# 2023-04-27
# 23년 4월 27일
# 등등 날짜를 표시하는 방법은 많다.
# import datetime
# today = datetime.datetime.today()
# print(today)
# strftime()
# print(today.strftime("%Y년 %m월 %d일"))
# %Y 년도 4자리 다 출력
# %y 년도 2자리 출력
# %m 월
# %d 일
# %H 시간(24시간)
# %i 시간(12시간)
# %M 분
# %s 초
# %A 요일
# print(today.strftime("%A"))

# time 라이브러리
# 시간 관련
# import time
# time_now = time.time()
# print(time_now)
# print(time_now.strftime("%H:%M:%S", time.localtime(time_now)))

# time.sleep()
# 프로그램이 잠깐 멈추었다가 다시 진행된다.
# 정확하게 시간을 재서 쉬는건 아니다. (하지만 유사함)
# 시간이 중요한 작업에서는 사용하지 않는게 좋다.
# import time    
# print("before")
# time.sleep(1)
# print("after")
# for i in range(10):
#     print(i)
#     time.sleep(1.2)

# math
# 수학관련
# import math
# math.ceil(1.1)   # 천장이라는 뜻, 올림하는 함수
# result = math.ceil(1.1)
# print(result)
# result = math.floor(1.9)  # 내림하는 함수
# print(result)
# 실수형일 때 소수점 뒤를 올림하냐 내림하냐의 차이
# print(math.pi)

# rendom
# 난수관련
# import random
# random.random()
# 0.0 ~ 1.0 사이의 실수 중 난수값을 무작위로 출력
# random_value = random.random()
# print(random_value)

#random.randint(시작, 끝)
# 시작 ~ 끝 사이의 정수 중 난수값을 무작위로 출력 (range와는 다르게 1 , 10 모두 포함) 
# random_value = random.randint(1, 10)
# print(random_value)

# random.choice(리스트)
# 리스트의 요소 중 무작위로 하나를 리턴
# foods = ["서브웨이", "맥도날드", "짜장면", "국밥", "김치찌개"]
# food = random.choice(foods)
# print(food)

# random.shuffle()
# 데이터는 그대로 있고, 순서만 바뀐다.
# li = [1, 2, 3, 4, 5]
# random.shuffle(li)
# print(li)
# random.shuffle(li)
# print(li)
# random.shuffle(li)
# print(li)

# lotto_numbers = list(range(1, 46)) 
# my_lotto = []
# for i in range(6):
#    random_value = random.choice(lotto_numbers) 
#    if random_value not in my_lotto:
#       my_lotto.append(random_value)
# print(my_lotto)

# in 연산자
# a in b 
# a가 b에 포함되어있으면 True
# a가 b에 포함되어있지 않으면 False


# not in 연산자
# a not in b
# a가 b에 포함되어 있지 않으면 True
# a가 b에 포함되어있으면 False

# li = [1, 2, 3, 4, 5]
# a = 10
# for i in li:
#    if a == i:
#       print("이미 있음")
#    else:
#       print("오류")


# if a in li:
#    print("이미 있음")

# 첫번째 식을 in 연산자를 사용하면 아래처럼 간단하게 축약할 수 있다.


# lotto_numbers = list(range(1, 46))
# random.shuffle(lotto_numbers)
# my_lotto = lotto_numbers[:6]
# print(my_lotto)

# 색 이름과 음식 이름을 합치면
# 멋진 밴드 이름이 니온다고 합니다.
# 색 이름과 음식이름을 무작위로 뽑아
# 밴드 이름을 추천하는 프로그램을 만들어보세요.
"""
연보라 보라 진보라 청보라 파랑  하늘 핑크 베이비핑크
떡볶이 소주 맥주 보드카 와플 아메리카노 솜사탕 아이스크림 
"""
# import random
# colors = ["연보라, 보라, 진보라, 청보라"]
# foods = ["떡볶이, 소주, 맥주, 보드카"] 
# color = random.choice(colors)
# food = random.choice(foods)
# print(f"{color} {food}")

# 재미있는 숫자야구 게임
# 1. 정답을 정한다. 정답을 4자리 숫자(랜덤)
# 2. 게임 유저가 정답을 입력한다.
# 3. 정답과 비교해서 S / B / OUT 개수를 알려준다
# 4. 정답을 맞추거나, 종료를 입력하면 끝낸다.
# 5. 답을 맞췄을 때 --> 한번 더 하시겠습니까?
# import random
# numbers = list(range(10))  # 0 ~ 9
# random.shuffle(numbers) 
# answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
# while True:
#     user_input = input("정답은?")
#     if user_input == "종료":
#           print("종료합니다.")
#           break
#     # 만약 숫자가 아닌값이 입력되면
#     # 다시 입력하게 한다.---> 처음으로 간다 --> continue
#     # isdigit() 숫자로만 이루어진 문자열인지 확인한다.   
#     # 숫자로만 이루어져 있으면 True 아니면 False
#     if not user_input.isdigit():
#         print("")
#         continue
#     # 만약 4자리 숫자가 아니면 다시 입력하게 한다.
#     # ----> 처음으로 간다 ---> continue
#     elif len(user_input) != 4:
#          print("4자리 숫자만 입력하세요.")
#          continue 
#     # 공백이 입력되면 어떻게 처리할까요
#     # "1234   "
    
#     # 첫글자가 0인 경우
#     elif user_input[0] == "0":
#          print("첫번째 숫자를 0이 아닌 다른수로 바꾸세요.")
#          continue
    
#     # 중복 확인
#     duplicate = False
#     for i in range(4):
#          if user_input[i] in user_input[i+1:]:
#             duplicate = True
#             break
#     if duplicate:
#          print("중복된 숫자가 없게 입력하세요.")
#          continue
#     strike = 0
#     ball = 0
#     out = 0
#     for i in range(4):
#             input_value = int(user_input[i])
#             if input_value not in answer:
#                   out += 1
#             elif input_value == answer[i]:
#                   strike += 1
#             else:
#                   ball += 1
#     print(f"strike: {strike}, ball: {ball}, out: {out}")

#     if strike == 4:
#         print("정답!!")
#         input("한번 더 하시겠습니까?[y/n]") 
#         if user_input == "y":
#             numbers = list(range(10))  # 0 ~ 9
#             random.shuffle(numbers) 
#             answer = numbers[1:5] if numbers[0] == 0 else numbers[:4]
#         else:
#               break
        
# 삼항 연산자
# 참일때값 if 조건 else 거짓일때값
# result = "참" if True else "거짓"
# result = "참" if False else "거짓"
# print(result)

# def is_odd_number(n):
    # return "홀수" if n % 2 == 1 else "짝수"

# os
# os 자원을 제어
# os : 운영체제 (operate system)
import os
# os.environ
# 환경 변수 값을 리턴한다.
# print(os.environ)  # 함수가 아니고 변수이기 때문에 괄호가 없다.

# os.getcwd()
# get current working directory
# 현재 작업 위치나 현재작업 공간을 가져오는 것
# print(os.getcwd())

# os.mkdir(디렉터리(폴더))
# 디렉토리(폴더)를 만든다.
# os.mkdir("폴더1")

# os.rename(원래이름, 바꿀이름)
# 파일의 이름을 바꾼다.
# os.rename("파일1","파일2")

# os.rmdir(디렉터리)
# 디렉터리(폴더)를 지운다
# 폴더안에 아무것도 없어야 함 (비어있어야 함)
# os.rmdir("폴더1")

# os.unlink(파일)
# 파일을 지운다.
# os.unlink("파일2")

# os.path
# os.path.exists("경로")
# 파일이 있으면 Ture, 없으면 False
# import os
# if not os.path.exists("없는파일"):
#     # open("없는파일", "w")
#     # f = close()
#     f = open("없는파일", "r")
# # f = open("없는파일", "r")
# else:
#     print("파일이 없습니다.")

# os.path.join("경로", "경로", "경로")
# 경로를 합쳐서 하나의 경로로 만들어준다.
# import os
# cwd = os.getcwd()
# my_folder = "python_study"
# file_name = "text_file.txt"
# file_path = os.path.join(cwd, my_folder, file_name)
# with open(file_path, "w", encoding="utf-8")as f:
#     f.write("테스트 파일을 작성합니다.")

# 외부 라이브러리
# 파이썬 표준 라이브러리가 아닌 라이브러리
# pip 를 사용해서 설치한다.

# pip 
# package installer for python
# 파이썬 모듈, 패키지를 설치하는 도구
# 파이썬 라이브러리에 있는 표준 라이브러리가 아니다.
# PyPi(Python Package Index) 파이썬 소프트웨어 저장공간
# PyPi에 있는 파이썬 패키지를 설치해준다.

# 패키지 설치(최신버전 설치)
# pip install 패키지 이름

# 패키지 삭제
# pip uninstall 패키지 이름 

# 특정 버전으로 설치 
# pip install 패키지 이름==1.0.5

# 최신 버전으로 업그레이드
# pip install -- upgrade 패키지 이름 

# 설치된 패키지 리스트 확인
# pip list 

# pip freeze
# 설치 후 기록해주는 것 