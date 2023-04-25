# 다음 함수를 정의하세요.
# 정수 n을 입력받고, n보다 
# 작은 수 중 3의 배수와
# 5의 배수를 모두 더한 합을
# 반환하는 함수
# 함수 이름 : sum_3_5

# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#     return result 

# def sum_3_5(n):
#     result = 0
#     for i in range(n):
#         if i % 3 == 0:
#             result += i
#         elif i % 5 == 0:
#             result += i
#     return result

# 위 두개는 같은 결과를 출력한다.

# 정육면체 주사위 2개가 있다.
# 2개의 주사위를 던졌을 때
# 나올 수 있는 주사위 눈의 조합을
# 모두 print하는 함수를 정의하세요.
# 함수 이름 : draw_dice
# 출력예시
# 1, 2
# 6, 3

# def double_dice():
#     for i in range(1, 7):  # 1 ~ 6 (1, 7을 넣어야 1 ~ 6 까지의 값을 가진다.)
#         for j in range(1, 7):   # 1 ~ 6
#             print(i,j)

# i = 1
# while i < 7:
#     j = 1
#     while j < 7:
#         print(i, j)
#         j += 1
#     i += 1
# # 두개는 같은 결과가 나온다. 


# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를
# 계산하고 반환하는 함수를 정의하세요
# 함수이름 : get_diff
# 파라미터 : a, b
# 반환값 : return
# 차이를 나타낸다고 할 때는 양수를 의미한다.

def get_diff(a, b):
    result = abs(a - b)
    if a > b:
        result = a - b
    else:
        result = a - b
    return result

# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개 정수(0 ~ 9, 중복가능)를
# 사용하여 만들 수 있는 가장 큰
# 수를 반환하는 함수를 정의하세요.
# 함수 이름 : get_biggest
# 파라미터 : a, b, c, d, e # 5개의 정수가 입력되어야 하니까 파라미터에 5개를 넣어준다.
# 반환값 : result
# 자릿수가 큰 곳에 큰 숫자가 와야 커진다.
# 정렬하는 문제로 볼 수 있다. 
# 위 문제는 큰 수가 앞에 오게 정렬하는 것.
# n 의 0 제곱은 무조건 1이다.

def get_biggest(a, b, c, d, e):  
    numbers = [a, b, c, d, e]
    numbers.sort()   # 오름차순으로 정렬
    result = 0
    for i in range(len(numbers)):   # 0 ~ 4  numbers 안에 숫자 다섯개가 있기 때문
        result += numbers[i] * (10 ** i)
    return result

    numbers = [a, b, c, d, e]
    numbers.sort(reverse=True)
    result = ""
    for i in numbers:
        result += str(i)
    return int(result)

# 위 방법 두가지 다 가능하다.

# 별찍기 2
# 정수를 함수에 입력하여
# 호출하면 해당 정수 줄의
# 별을 화면에 출력한다.
# 함수 이름 : print_stars2
"""
출력 결과
n -> 1
*
n -> 4
   *
  **
 ***
****
"""
def print_stars2(n):    # return이 필요없는 함수니까 생략한다.
    for i in range(1, n + 1):     # 1 ~ n     # 정수형이니까 파라미터는 n 으로 설정한다. 
        print(" " * (n - i) + "*" * i)   # 여기서 i는 별의 개수
print_stars2(10)


        