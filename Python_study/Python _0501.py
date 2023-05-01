# # a = [5, 4, 3, 2, 1]
# # b = a[:]
# # print(id(a),id(b))

# import copy
# a = [1, 2, 3, 4, 5]
# b = copy.deepcopy(a)
# print(a,b)

# a = 100
# if a > 0 or (a % 2) != 0:
#   print('a is even')
# # | : 비트 연산자로 작동된다.

# 3 and 4
# # = 숫자에서는 무조건 작은게 나온다.

# 3 & 4 # & : 논리연산자가 X -> 비트연산자로 작동된다.
# # 0011  & 0100 -> 0000

# 3 or 4
# # = 3

# 3 | 4
# # = 7

# b 로 a를 나눈 나머지가 3 초과면 실패, 3이면 무승부, 3미만이면 성공이 출력되도록 만들어보자 

# a= 34
# b = 4
# r = a%b
# if r < 3:
#     print("실패")
# if r == 3:
#     print("무승부")
# else:
#    print("성공")

# 무슨 학교 다니세요?
# 태어난 년도를 계산하여 학교종류를 맞추는 프로그램
# 나이는 현재년도 - 태어난년도 +1 로 계산
# 26세 이하 20세 이상이면 "대학생", 20세 미만 17세 이상이면 "고등학생"
# 17세미만 14세 이상이면 "중학생", 14세 미만 8세 이상이면 "초등학생"
# 그 외의 경우는 학생이 아닙니다 출력
 
# birth_year = int(input("당신이 태어난 년도를 입력해주세요."))
# age = 2023 - birth_year+1
# message = ""
# if 20 <= age and age < 26:
#     print("대학생")
# elif 17 <= age and age < 20:
#     print("고등학생")
# elif 14 <= age and age < 17:
#     print("중학생")
# elif 8 <= age and age < 14:
#     print("초등학생")
# else:
#     print("학생이 아닙니다.")

# 양의정수 하나를 입력받아 이 정수가 2의 배수인지 3의 배수인지 작성하세요

# num = int(input("정수를 하나 입력하세요."))
# if num % 2 ==0:
#     if num % 3 ==0:
#         print("2와 3으로 나누어집니다.")
#         else:
#         print("2로 나누어 집니다.")
# elif num % 3 == 0:
#     print("3으로 나누어 집니다.")
# else:
#     print("어느것으로도 나누어 지지 않습니다.")

# [5, 4, 3, 2 ,1 0]
# count = [5, 4, 3, 2, 1, 0]
# for i in range(5, -1, -1):
#     print(count)
# 하나씩 작아지므로 -1 이 나온다.
 
# range 함수를 이용하여 1부터 10까지의 합을 구하세요

# for i in range(1, 11):
#     sum = sum + 1
#     print(sum)

# 별찍기
# 계단형, n을 입력받아, n만큼 줄을 만들고 계단 형태로 별찍기
# 삼각형, 왼쪽 아래가 직각인 n만큼의 높이를 가지는 직각삼각형
# 오른쪽 아래가 직각인 n만큼의 직각삼각형
# 역삼각형, 왼쪽 위가 직각인 n만큼의 높이를 가지는 직각삼각형
# 오른쪽 위의 직각인 n만큼의 높이를 가지는 직각삼각형
# 피라미드, n만큼의 높이를 가지를 홀수개의 별 피라미드

# 계단형
# n = int(input("n : 1"))
# for i in range(n):
    # print("" * i, end = "")
    # print("*" * n)

# 삼각형
# n = int(input('n:'))
# for i in range(1, n + 1):
#     print('*' *i)

# 역삼각형
# n = int(input('n:'))
# for i in range(n):
#     print('*' * (n - i))

# n = int(input('n:'))
# for i in range(' ' * i, end=''):
#     print('*' * (n - i))

# 피라미드
# n = int(input("n:"))
# for i in range(1, n + 1):
#     print(" " * (n - i), end = "")
#     print("*" * (2 * i - 1))

# x = [3, 6, 9, 20, -7, 5]의 값의 모든 요소에 10을 곱한 뒤 출력하세요
# 심화 : 출력과 리스트 x의 값에도 모두 10을 곱해주세요
# y = {"math" : 70, "science" : 80, "english" : 20} 의 값의 모든 요소에 10을 더한 뒤 출력하세요
# 심화 : 출력과 딕셔너리 y의 값에도 모두 10을 더해주세요
# 숫자를 입력받고 입력받은 정수의 구구단을 출력하세요 

# # 1
# x = [ 3, 6, 9, 20, -7, 5]
# for i in x:
#     print(i * 10)

# # 1번 심화
# for i in range(0, len(x)):
#     x[i] = x[i] * 10
# print(x)

# # 2
# y = {"math" : 70, "science" : 80, "english" : 20}
# for key in y:
#     val = y[key]
#     y[key] = y[key]+10
#     print('%s : %d' %(key, val + 10))

# 1 ~ 100 임의의 숫자를 맞추세요
# import random
# true_value = random.randint(1, 100)
# input_value = 99999 # 임의의 값 할당
# print("숫자를 맞춰보세요")
# while true_value != input_value:
#     input_value = int(input())
#     if input_value > true_value: # 사용자의 입력값이 true_value 보다 클 때
#         print("숫자가 너무 큽니다.")
#     else:
#         print("숫자가 너무 작습니다.") # 사용자의 입력값이 true_value 보다 작을 때
# print(f"정답입니다. 입력한 숫자는{true_value} 입니다.")

# word = ["school", "game", "piano", "sience", "hotel", "mountain"] 
# # 중 글자수가 6글자 이상인 문자를 모아 새로운 리스트를 생성하세요
# a = list()
# for i in range(len(word)):
#     if len(word[i]) >= 6:
#         a.append(word[i])
# print(a)
# 들여쓰기 항상 주의하기

# 1 ~ 100 까지 숫자 중
# 3과 5의 공배수일 경우 "3과 5의 공배수"
# 나머지 숫자 중 3의 배수일 경우 "3의 배수"
# 나머지 숫자 중 5의 배수일 경우 "5의 배수"
# 모두 해당되지 않을 경우 그냥 숫자를 출력하세요.
# 심화 : 1 ~ 입력한 숫자까지의 숫자 중 음수 출력, 뭐더라?

# b = int(input("정수를 입력하세요."))
# if b <= 0:
#     print("음수는 정의하지 않음")
# else:
#     for i in range(1, b + 1):
#         if i % 3 == 0 and i % 5 == 0:
#          print("3과 5의 공배수")
#         elif i % 3 == 0:
#          print("3의 공배수")
#         elif i % 5 ==0:
#          print("5의 배수")
#         elif i <= i <= 100:
#            print(i)
#         else:
#            print("1과 100 사이의 숫자가 아닙니다.")


# 사용자로 부터 숫자를 계속 입력 받다가 s or S 를 입력하면 합계 출력
# c = 0
# d = 1
# while(d == 1):
#    a = input()
#    if (a == 's' or a == 'S'):
#       d = 0
#    else:
#       a = int(a)
#       c += a
# print(c)

# 행은 가로 열은 세로
# 평균 구하기 
kor_score = [39, 69, 20, 100, 80]
math_score = [32, 59, 85, 30, 90]
eng_score = [49, 70, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]
student_score = [0, 0, 0, 0, 0]

i = 0
for subject in midterm_score:  # kor, math, eng 과목선택
    for score in subject:  # 과목선택후
        student_score[i] += score
        # print(subject, score, "i", i.student_score)  # kor -> math -> eng
        # i += 1 # 학생 index구분
    # i = 0 # 과목이 바뀔 때 학생 인덱스
else:
    a, b, c, d, e = student_score
    student_average = [a / 3, b / 3, c / 3, d / 3, e / 3]
    print(student_average)
