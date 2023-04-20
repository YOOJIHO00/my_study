# whlie 반복문
# 동일한 동작을 여러번 반복하여 수행하기 위해 사용
"""
whlie(~하는  동안 이라는 뜻) 조건 : 
    반복할 코드 
"""
# 조건이 Trur(참)인 경우에 코드를 계속 반복
# ptint(1)
# print(2)
# print(3)
# print(4)
# print(5)
# print(6)
# print(7)
# print(8)
# print(9)
# print(10)

# n = 1
# while n <= 10:
#     print(n)
#     n += 1   #n = n + 1

#  += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# + = n += 1 은 n = n + 1 이라는 의미
# - = 
# * = 
# / =
# ** =
# // = 
# % =

# s1 = "안녕"
# s1 += "하세요"  #s1 = s1 + "하세요" 

# # while 반복문을 활용하여 10부터 1 까지 순서대로 출력하세요.

# cnt = 10
# while cnt >= 1:    #(while cnt >= 0: 똑같음)
#     print(n)
#     cnt -= 1

# money = 10000
# price = 1000
# coffe = 5
# while money >= price:
# # while money - price >= 0:
#     print("커피를 구매했습니다.")
#     money -= price
#     coffe -= 1
#     print("남은 커피:", coffe)
# if coffe == 0:
#     break 

# break
# 반복문에서 자주 사용되는 키워드
# 반복문을 즉시 종료한다.
# 조건을 따지지 않는다.
# 보통 if문과 함께 사용함

#while 반복문을 활용하여 1부터 10까지 홀수만 출력한다.
# while b <= 10:
#     if b % 2 == 0:
#         b += 1
#         continue
#     print(b)
#     b += 1

# # 연산이 일어난 위치와 조건을 생각해서 적어야 한다.

# continue
# while 반복문의 제일 처음으로 돌아감
# b = 0
# while b <= 9:
#     b += 1
#     if b % 2 == 0:
#         continue
#     print(b)
    
# 무한반복문 (무한루프)
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다.
# while True:
#     user_input = input("종료하려면 1을 입력해주세요.")
#     if user_input =="1":
#         break

# 무한반복문으로 계산기 만들기
# +, -, *, / 계산
# # 2개의 수를 계산 예) a + b
# while True:
#     print("""
#     계산기
#     ======
#     1. 더하기(+)
#     2. 빼기(-)
#     2. 곱하기(*)
#     4. 나누기(/)
#     """)
#     operator = input("계산을 선택하세요 : ")
#     if operator == "1":
#         print("1 + 2 =", 1 + 2)
#     if operator == "2":
#         print("1 - 2 =", 1 - 2)
#     if operator == "3":
#         print("1 * 2 =", 1 * 2)
#     if operator == "4":
#         print("1 / 2 =", 1 / 2)

# 코드를 수정해서 사용자가 입력한 숫자를 이용해 계산하도록 변경하세요.
# q를 입력하면 종료되도록 변경하세요.

# while True:
#     print("""
#     계산기
#     ======
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     """)
#     operator = input("계산을 선택하세요.")
#     a = int(input("숫자를 입력하세요."))
#     b = int(input("숫자를 입력하세요."))
#     if operator == "1":
#         print(a, "+", b, "=", a + b)
#     if operator == "2":
#         print(a, "-", b, "=", a - b)
#     if operator == "3":
#         print(a, "*", b, "=", a * b)
#     if operator == "4":
#         print(a, "/", b, "=", a / b)
#     if operator == "q":
#         break

# a = 1
# if a == 2:
#     print(2)
# else:
#     if a == 3:    #elif를 사용하는게 더 효율적이다.(else + if = elif)
#         print(3)
#     else:
#         print(1)

# 사용자가 가지고 있는 돈을 입력 받는다.
# 구매할 수 있는 커피의 개수와
# 잔돈을 출력한다.
# 구매할 수 있는 음료수의 개수와 잔돈을 출력한다.
# 구매할 수 잇는 콜라의 개수와 잔돈을 출력한다.
# 커피는 500원 음료수는 700원 콜라는 930원
# 물품의 개수는 무한하다고 가정한다.
#  while 반복문을 사용하여 작성한다.

# idx = 0
# prices = [500, 700, 930]
# money = int(input("돈:"))
# while idx <= len(prices):   #while idx < 3:  
#     price = prices[idx]    #500 이유는 0번 인덱스 이기 때문이다
#     print(money // price)
#     print(money % price)
#     idx += 1 

# while 반복문을 사용해서 
# scores 리스트에 시험점수 5개를 정수형으로 입력 받으세요.


# scores = []
# n = 0
# while n < 5:
#     scores = int(input("시험점수:"))     #정수형이니까 int 로 바꿔줌
#     scores.append(score)
#     n += 1
#     print(scores)

# while 반복문을 사용하여
# 구구단 2단을 출력하세요.

n = 1
while n < 10:
    print("2 *", n, "=", 2*n)
    n += 1

