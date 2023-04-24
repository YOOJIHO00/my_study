# function 함수
# 입력 -> 처리 -> 출력
# input(입력)을 받아서
# 특정 작업을 수행하고
# output(출력)을 반환한다.

# 내장 함수 (built-in)
# 파이썬이 기본적으로 
# 제공해주는 함수
# print()
# len()
# zip()
# int()
# float()
# str()
# list()
# range()

# abs()
# absolute의 약자
# 입력한 숫자형 데이터의
# 절댓값을 반환한다. 
# 수가 가지고 있는 그 값 자체를 뜻한다. (부호 없이)
# print(abs(100))  #100
# print(abs(-100))  # 100
# print(abs(3.15))  # 3.15
# print(abs(-3.15))  # 3.15

# sum(리스트)
# 리스트 안의 숫자를 
# 모두 더한 값을 반환한다.
# sum([1, 2, 3, 4, 5])    
# print(sum([1, 2, 3, 4, 5]))  #15

# max(리스트)
# 리스트 안에서 최댓값을
# 찾아 반환한다.
# max([1, 2, 3, 4, 5])
# print(max([1, 2, 3, 4, 5]))  # 5

# # min(리스트)
# # 리스트에서 최솟값을
# # 찾아 반환한다.
# min([1, 2, 3, 4, 5])
# print(min([1, 2, 3, 4, 5]))  # 1

# # chr(정수)
# # 정수 1개를 입력받고 해당하는
# # 유니코드 문자를 반환한다.
# print(chr(65))  # A

# # ord(문자)
# # 문자 1개를 입력받고 해당하는
# # 정수를 반환한다. 
# print(ord('A'))  # 65

# # round(값)
# # round(값, 소수 자릿수)
# # 반올림 함수 ( 0 ~ 4  까지는 내림, 5 ~ 9 까지는 올림)
# print(round(1.234))   # 1
# print(round(1.234, 2))  # 1.23
# print(round(1.369, 1))  # 1.4

# 함수정의(define)
# 함수 이름
# 함수 입력값 (paramiter)
# 함수 결괏값 (return value)

"""
def함수이름(함수입력값):
    함수기능코드
    return 함수 결괏값
"""
# def는 함수를 정의하는 명령어
# 함수 이름도 변수 이름처럼 
# 규칙을 지켜서 지어야 한다.
# 영어, 숫자, _ 만 사용
# 숫자로 시작하면 안된다.
# 띄어쓰기 하면 안된다.
# 키워드 사용하면 안된다.
# 기존에 이미 정의된 함수의
# 이름도 피하는것이 좋다.

# def print_names():   # 괄호를 비우면 입력값이 없는 함수라는 뜻
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")   # 출력값 이 없는 함수
# print_names()  

# def get_name():
#     return "유지호" # 출력값이 있는 함수  

# def print_my_name():  
#     print(get_name())  
# print_my_name()   # 유지호가 출력된다.

# print_my_name()
# a = print_names()  # return이 없다.
# b = get_name()    # return이 있다. 
# print(a)
# print(b)
# return이 없으면 나오는 값(반환값)이 없다.

# paramiter
# 함수에 입력하는 값
# 매개변수, argment 혼용

# def add(a, b):   # 괄호안에 들어있는 값이 paramiter
#     return a + b

# def print_add(a, b):
#     print(a + b)
# result = add(1,2)
# print(result)   # 3

# result = print_add(1,2)
# print(result)  # None  = return이 없는 함수이기 때문이다. 
# a 와 b 의 값을 정의하지 않고 호출하면 에러가 난다.

# print_add("안녕", 1) # Erorr
# print_add(1, 2)
# print_add("안녕", "하세요.")
# print_add("하세요.", "안녕")
# print_add(b= "하세요.", a ="안녕")

# 쉼표로 구분을 해서 순서대로 위치에 따라 전달 받는다.
# 위치와 순서를 신경을 써줘야 한다.
# 숫자열과 문자열은 서로 더하기가 안된다.
# 그래서 문자열과 숫자를 같이 넣으면 에러가 난다. 
# 마지막 같은 변수에 넣으면 안녕하세요가 출력된다.
# 매개변수 이름에 값을 할당할 수도 있다.

# def swap_number(a, b):
#   temp = a    # temp 는 "임시" 라는 뜻. 변수를 하나 만들어서 a값을 저장했다가 b에 넣는것.
#   a = b       # '지역변수' 라고도 부른다. (코드 전역에서 사용되는 변수) 
#   b = temp
#   print(a, b)
#   return a, b   # 로 고치면 실행된다. 
# # a = 1 
# b = 2
# print("함수 호출 전", a, b)
# a, b = swap_number(a, b)
# print("함수호출 후", a, b)
# print(a, b)
# 함수 안에서 쓰는 a, b와 함수 바깥에서 쓰는 a, b 는 다르다. 
# 이름만 똑같고 서로 다른 변수이다.
# if문 같이 블럭으로 구분짓는 애들은 다 이 조건을 받는다. 

# 함수를 정의하세요.
# 함수 이름 : mul
# 함수 입력값 : 정수 2개
# 함수 출력값 : 정수 2개의 곱

# def mul(n1, n2):
#     return n1 * n2 
# print(mul(1, 2))

# result = mul(1,2)
# print(result)
# 위 두개는 같은 답이 나온다 (똑같은거임)

# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3
# d, e, f = [4, 5, 6]
# a, b = 1, 2
# temp = a
# a = b
# b = temp
# a, b = b, a
# g, h, i = (7, 8, 9)
# 파이썬은 세개의 식을 한 줄로 합칠 수 있다.(쉼표로 여러개를 한꺼번에 넣는것)

# 기본 값 매개변수
# default value parameter
# 함수 호출 시 n2에 입력된 값이 없으면,
# 기본 값 사용
# def mul(n1, n2 = 1):
#     return n1 * n2

# mul(1,2)
# mul(1)


# def test_func(x, test=[]):
#     test.append(x)
#     print(x, test)

# test_func(1)  # 1[1]
# test_func(2)  # 2[1, 2] 
# # 기본값으로 리스트는 쓰면 안된다.
# # 리스트가 다시 생성되는 게 아니고 계속 또 사용되기 때문에
# # 내가 예측하는 결과와 다르게 출력된다.

# def test_func1(x, test=[5]):
#     test = test
#     print(x, test)

# test_func1(1)   # 1[5]  기본값이 정수형이라 바뀌지 않는다.
# test_func1(2)   # 1[5]  리스트에 대한 사용법 꼭 생각하기.

# def test_func2(x, test = None):
#     if test == None:
#         test = []
#     test.append(x)
#     print(x, test)    
# 리스트를 새로 만든거랑 다른거다.
# 기본값으로 리스트는 쓰지 말 것.

def sub(n1, n2, n3):
    print(n1 - n2 - n3)
# 기본값이 설정된 매개변수들은 
# 기본값이 없는 매개변수보다 뒤에 위치해야 한다.
# 지키지 않으면 에러가 난다.
# 위에서 만약에 n2 =0 을 넣고 싶다면, 
# n3 보다 뒤로 보내야 한다.

# 1 ~ 10 까지 더한다.
# * 를 사용한 매개변수
# 입력값이 몇개가 될 지
# 모를 때 (안정해졌을 때) 사용하게 된다.
# def add_many(*args):  #arguments의 줄임말
# # add_many(1,2) ---> 3
# add_many(1, 2, 3, 4, 5) ---> 15
# add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) ---> 55
def add_many(*args):
    # 튜플처럼 사용한다.
    # 인덱싱, 슬라이싱
#     result = 0
#     for i in args:
#         result += i
#     return result 
# result1 = add_many(1, 2, 3, 4, 5)
# print(result1)
# result2 = add_many(3, 2, 5, 9, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)

# def calc_many(n1, *args):  # def calc_many(arge*,n1): 이렇게 해도 된다.
#     result = n1            # 일반 매개변수랑 같이 사용 가능 하다.
#     for i in args:
#         result += i
#     return n1

# 키워드 매개변수
# **kwargs
# keyword arguments 
# 딕셔너리로 사용 
 def print_kwargs(n1, *args, **kwargs):  # 뒤에 오는 값들이 유동적일 때 많이 사용한다.
    print(kwargs)

# print_kwargs(a=1, b=2)
# print_kwargs(name = '이름', age = 10) 

# 함수의 반환
# return 반환값
# retnrn을 만나면 반환값을
# 반환함과 동시에 함수가 종료된다.
# def test_func5():
#      print(1)
#      print(2)
#      return None   # 아래 세개는 실행이 되지 않고 종료된다.
#      print(3)
#      print(4)
#      print(5)
# #  함수의 반환값은 무조건 1개 이다.
# def test_func6(a,b):
#     return a + b, a * b
#     # return (a + b, a * b) 와 같다. 
#     # 값을 여러개 반환하고 싶으면
#     # 리턴 뒤에 쉼표를 써서 한 줄로 이어줘야 한다.
# print(test_func6(1,2))
# result_add, res_mul = test_func6(1,2)
# # res_add, res_mul = (a+b, a*b) # 바로 위 식이랑 똑같은 의미이다. 
# print(result)
# print(res_add, res_mul)

# 홀수 판별 함수
# 정수 1개를 입력받고 홀수인지 판별하는 함수
# 함수이름 : is_odd_number
# 파라미터 : n
# 반환값 : 홀수면 True, 짝수면 False

# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     else:
#         return False
# is_odd_number(5)
    
# def is_odd_number(n):
#     if n % 2 == 1:
#         return True
#     return False
    
# def is_odd_number(n):
#     return n % 2 == 1

# 세개 다 같은 결과가 나온다. 
# 첫번째부터 점점 간단해지는 식을 적은것이다.
# 위같은 함수들은 True, False 를 return 하는 함수인 경우가 많다.

# 테두리를 출력하는 함수
# 문자열을 입력받고 print함수를 이용해
# 테두리와 함께 문자를 출력(print)한다.
# 함수이름 : get_bordered_str
# 파라미터 : messege
# 반환값(return) : None
# print예시
# """
# *****
# hello
# *****
# """

# def get_bordered_str(message):
#      n = len(message)  
#     print("*" * n)
#     print(message)
#     print("*" * n)
# get_bordered_str("hello")
# get_bordered_str(12345)  # Erorr , len 함수에는 숫자형을 사용할 수 없다.

# def get_bordered_str(message):
#     message = str(message)
#     n = len(message)  
#     print("*" * n)
#     print(message)
#     print("*" * n)
# get_bordered_str(12345)
# 이렇게 해주면 에러가 안난다.

# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면 (초 당 몇 미터 갔는지)
# km/h 단위의 속도로 변환한다. (시간 당 몇 미터 갔는지)
# 함수이름 : convert_velocity
# 파라미터 : velocity
# 반환값 : km/h로 변환된 속도

def convert_velocity(velocity):
    # 1초에 1m -> 1m/s
    # 1m/s로 한시간동안 가면 몇 m?
    # 1m/s * 3600(1시간)
    # 3600m/h
    # 1km는 몇 m? 1000m
    # 3600m/h는 몇 km/h?
    # 3600m/h 는 1000(1km)
    # 1m/s ==> 3.6km/h
    # 1m/s * 3600 / 1000 ==> 3.6km/h
    # 초속 * 3600 / 1000 ==> 시속
    # 초속 * 3.6 = 시속
#    result = velocity * 3.6
#    return result 
# velocity = convert_velocity(10)
# print(velocity)
 """
 출력결과 n -> 1
 별찍기 함수
 *
 **
 ***
 ****
 """
# 정수를 함수에 입력하여
# 호출하면 해당 정수 줄의
# 별의 화면을 출력한다.
# 함수 이름 : print_stars
# 파라미터 : n
# 반환값 : None
def print_stars(n):
    for i in range(n):  # 0 ~ n - 1
        for j in range(i + 1):   # 0 ~ i
           print("*", end="")  # end 라는 값에 기본값으로 줄바꿈을 넣어준 것이다.  
        print()  # 아무것도 출력 안하고 end의 기본값(줄바꿈)을 출력한다.
    i = 0
    while i < n:
       j = 0 
       while j < i + 1:
          print("*", end="")
          j += 1
          print()
          i += 1
print_stars(4)

