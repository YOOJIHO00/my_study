# 5월 2일 


# def swap_value(x, y):
#     temp = x
#     x = y
#     y = temp


# def swap_offset(offset_x, offset_y):
#     temp = a[offset_x]
#     a[offset_x] = a[offset_y]
#     a[offset_y] = temp



# def swap_refernce(list, offset_x, offset_y):
#     temp = list[offset_x]
#     list[offset_x] = list[offset_y]
#     list[offset_y] = temp

# a = [1, 2, 3, 4, 5]
# swap_value(a[1], a[2])
# print(a)

# swap_offset(1, 2)
# print(a)

# swap_refernce(a, 1, 2)
# print(a)

# 이 함수는 두개의 숫자를 input으로 받으면 작은수로 큰 수를 
# 나눈 몫과 나머지를 반환하는 함수이다.
# 반환값은 튜플로 되어있으며, 몫, 나머지 순으로 되어있다
# 단, 0으로 나누는 것은 불가하기 때문에 두 수 중에 작은수가
# 0이라면 화면에 "0은 사용할 수 없습니다."를 출력하고 종료되어야 한다.
# abs = absolute = 절댓값 = 허수


# def div3(a, b):
#     if a < b:
#         big = b 
#         small = a 
#     elif a <= b:
#         big = a
#         small = b
#     else: 
#         print("정수가 아닙니다.")
#     if small == 0:
#         print("0은 사용할 수 없습니다.")
#     elif abs(big) < 0 or abs(small) < 0:
#         print("정수를 입력해주세요.")
#     else:
#         q = big // small
#         r = big % small
#         return(q, r)


# 어떠한 string을 받으면 일정한 단위로 끊어서 화면에 출력하는
# 함수를 짜보자 출력하는 단위는 따로 정하지 않으면 2로 설정해보자
# 힌트 : input을 string과 unit = 2 로 받고
# while을 사용하고, 길이는 ,len함수를 사용하도록 하자.

# def func(string, unit = 2):
#     i = 0
#     while i < len(string):
#         print(string[i:] + unit)
#         i += unit
      


# def test(*args):
#     print(args)

# test(1, 2, 3, 4, 5)

# add_all 함수를 짜봅시다.
# 힌트 : *kargs를 input으로 받으세요.
# 튜플형 말고 리스트 형으로도 받아보기
# add_all(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def add_all(*inputs):
#     s = 0
#     for i in range(len(inputs)):
#         s += inputs[i]
#     return s 

# def add_all2(*inputs):
#     return sum(inputs)

# def add_all3(*args):
#   s = 0
#   for i in args:
#     for j in j:
#       s += j 
#     return s
  
# def add_all4(*args):
#   temp = 0
#   for i in range(len(args)):
#     if type(args[i]) == list:
#       for j in args[i]:
#         temp += j
#       else:
#         temp += args[i]
#     return temp
# vs 코드는 print 해야 출력되는데 시간에 쫓겨서 내가 못쓴거

# 팩토리얼(Factorial)을 구하세요.
# 1부터 시작해서 어떤 범위에 있는 모든 정수를 곱하는 것


# # 재귀적으로 하지 않은 것
# def fact(n):
#     f = 1  # 곱을 계산할 변수의 초깃값
#     for i in range(1, n + 1):
#         f = f + i # 곱셈연산
#     return f

# # 재귀적으로 하는 것
# def fact(n):
#     if n <= 1:  # n이 1 이하이면 종료조건
#         return 1
#     return n * fact(n - 1)

# 사람이름으로 되어있는 리스트를 받아서 "대기번호 ?번 : 사람이름"
# 을 화면에 출력하고 (번호표, 사람이름)을 원소로 이루어진 리스트를 반환한다.

# people = ["펭수", "뽀로로","뚝딱이", "텔레토비"]
# def func1(line):
#     new_lines = []
#     i = 1   # 대기번호를 트래킹 하는 변수 i
#     for x in line:
#         print("대기번호 %d번 : %s" %(i, x))
#         new_lines.append((i, x))
#         i += 1  # 별도로 업데이트를 해줘야 함
#     return new_lines

# enumerate = 열거하다
# 반복가능한 객체의 인덱스와 원소에 함께 접근할 수 있는 함수

# lst = ["a", "b", "c"]
# for x in enumerate(lst):
#     print(x)

# people = ["펭수", "뽀로로","뚝딱이", "텔레토비"]
# def func1(line):
#     new_lines = []
#     for idx,val in enumerate(line):
#         print("대기번호 %d번 : %s" %(idx, val))
#         new_lines.append((idx, val))
#     return new_lines

# zip 반복가능한 객체들을 (2개 이상) 병렬적으로 묶어주는 함수
# 각 원소들을 튜플의 형식으로 묶어준다

# str_list = ["one", "two", "three", "four"]
# num_list = [1, 2, 3, 4]
# for i in zip(num_list, str_list):
#     print(i)

# lambda(람다)
# def plue_two(num):
#     return num + 2
# a = 2
# b = plue_two(a)
# print(b)

# lambda x :  x + 2
# func2 = lambda x : x + 2
# c = func2(2)

# # map (함수, 자료형)
# # 리스트, 튜플, 스트링 등 자료형 각각의 원소에 동일한 함수를 적용
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i * i)
# print(squared)

# squared_map = list(map(lambda x : x ** 2, items))
# print(squared_map)

# # iambda와 map을 이용하여 items의 요소들을 string(문자)로 바꾸는 것을 짜봅시다.
# items = [1, 24, 3, 6, 7]
# str_items = list(map(lambda x : str(x), items))
# print(str_items)

# list comprehension
# 0 ~ 9 까지를 순서대로 가지고 있는 리스트를 만드세요.
# list_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# list_2 = []
# for x in range(10):
#     list_2.append(x)
# print(list_2)

# lc_1 = [x for x in range(10)]
# print(lc_1)

# 구구단 2단
# tables = [2 * x for x in range(1,10)]
# print(tables)

# 10부터 20까지의 숫자들 중에서 짝수만을 담은 리스트 만들기
# list3 = []
# for x in range(10, 21):
    # if x % 2 == 0:
        # list3.append(x)
    # print(list3)

# lc_2 = [x for x in rnage(10, 20) if x % 2 ==0]
# print(lc_2)

# 258p1)
# lc_3 = [x ** 2 for x in range(1, 11) if x ** 2 < 50]
# print(lc_3)

# lc_4 = [s for s in sentence.split() if len(s) < 5]
# print(lc_4)

# 1부터 10까지의 숫자들 중 홀수면 어떤 제곱수를,
# 짝수이면 세제곱수를 담은 리스트를 출력하세요

# list_4 = []
# for x in range(1, 11):
    # if x % 2 == 1:
        # list_4.append(x ** 2)
    # else:
        # list_4.append(x ** 3)

# [x ** 2 if x % 2 == 0 else x ** 3 for x in range(1, 11)]

# for문 + for문
# word1 = "Hello"
# word2 = "World"

# result = [i+j for i in word1 for j in word2]
# print(result)

# list_5 = [23, 67, 32, 48, 19, 57, 29, 49]
# lc_6 = [x * 5 if x <= 40 else 41 for x in list_5]
# lc_6

# stdents = ["보라돌이":61, "뚜비":35, "나나":78, "뽀":88]
# result = [(name, True) if score > 60 else (name, Flase) for name, score in students.items()]
# result

# from time import time

# import time
# start = time.time()  # 시작시간저장
# python_list = [x ** 3 + 10 for x in python_list]
# print("time:", time.time() - start)  # 현재시각 - 시작시간 = 실행시간 

# 백터화
# 배열은 for문을 작성하지 않고 데이터를 일괄처리 하는 것
# arr = np.array([1, 2, 3],[4, 5, 6])
# arr
# arr + arr
# arr / arr

# 브로드캐스팅
# 다른 모양의 배열간의 산술연산을 수행할 수 있도록 해주는 numpy의 기능
# arr2 = np.array([100, 200, 300])

# dtype
# 배열에 담긴 원소의자료형(ndarray는 같은 자료형을 담음)

# size
# 배열의 원소의 개수

# arr.ndim
# 배열의 차원의 개수

# arr.shape

# 0차원(상수)
# import numpy ao np
# a = np.array(10)
# print(a)
# print(a.ndim)
# 결과를 출력하면 0이 나온다(0차원)

# 1차원
# a = np.array([1, 2, 3])
# print(a)
# print(a.nidim)
# 결과를 출력하면 1이 나온다(1차원)

# 2차원
# a = np.array([1, 2][3, 4])
# print(a)
# print(a.ndim)

# 3차원
# a = np.array([[1, 2], [3, 4]])
# print(a)
# print(a.ndim)
# print(a.shape)

# 대부분 2차원을 사용한다
# 고차원이지만 끌어내려서 사용한다

# range함수를 이용
# arr1 = np.array(range(20))
# arr1
# arr = np.arange(20)
# arr2

# np.zeros

# np.ones

# np.full

# np.empty

# np.inspace
 
# 배열결합함수
# hstack, concate(ezis = 0)
# 두 배열을 왼쪽에서 오른쪽으로 붙이기
# arr.hstack([a, b])
# a = np.array([1, 2, 3])
# b = np.array([4, 5, 6])

# np.hstack([a, b])
# np.concatenate((a, b).axis = 0)

# vstack.concatenete(axis=1)   # 1D vector는 안된다.
# np.vstack([a,b])

# 두 배열을 위 아래로 붙이기
# np.column_stak([a, b])

# import.random
# random.random() 0 <= 리턴값 => 1

# seed
# 난수 초기값 부여 -> 재현가능성(Reporducilbility)

# np.random.rand
# 정규분포

# 로또번호 만들기
# import numpy as np
# def make_lotto(count):
#     for i in range(count):
#         lotto_num = []    # 로또번호가 담길 리스트형 변수
#         for j in range(6):
#              lotto_num = np.random.choice(range(1, 46),6,replace=False)
#              lotto_num.sort()
#         print("{}, 로또번호 : {}", format(i + 1, lotto_num))
#     count = int(input("로또 번호를 몇 개 생성할까요?"))
#     make_lotto(count)
