# for 문
# 무한반복이 안된다 (무한반복은 while 에서만 가능) 
""""
for 변수 in iterable(순회 가능하다는 뜻):
    반복할 코드
"""
# li_1 = ["one","two","three"]
# for i in li_1:
#     print(i)
# # 첫번째 요소부터 마지막 요소까지 변수에 대입하면서 반복

# s1 = "hello"
# for i in s1:
#     print(i)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for number in numbers:
#     print(number)
# numbers.reverse()
# for number in numbers:
#     print(number)

# range() (범위라는 뜻)
# 숫자 range 객체를 만들어주는 함수
# range(끝 정수)
# 0 끝 ~ 정수 -1
# for i in range(10):   # 0 ~ 9
#     print(i)
# 시작 ~ 끝 -1
# range(시작, 끝)
# for i in range(1, 11):   # 1 ~ 10
#     print(i)
# # range(시작, 끝, 스텝)
# for i in range(1, 21, 2):   
#     print(i)
# 시작 ~ 끝 -1 까지 인데 스텝만큼 차이나게


# for문을 사용하여 2부터 30까지 출력해보세요

# for i in range(2, 31):
#     print(i)

# # for문을 사용하여 2부터 30까지 숫자 중 짝수만 출력해보세요.

# for i in range(2, 31):   #2 ~ 30 
#     if i % 2 == 1:   #홀수
#         continue
#         # pass #아무것도 안하고 그냥 넘어갈 때 
#     else: #짝수
#         print(i)

# for i in range(2, 31, 2): # 2 ~ 30 까지 2씩 차이 
#     print(i)

# for i in range(2, 31):
#     if 1 % 2 == 0:   # 짝수  
#         print(i)

# if 1 == 1:
#     pass
# print("완료")

# for i in range(5):     #이렇게 아무것도 하지 않고 넘어갈 때 pass 를 사용한다. 
#     pass
# print ("완료")

# for문을 사용하여 10부터 1까지 출력해보세요

# for i in range(10, 0, -1):     #가운데 숫자가 0인 이유는 첫번째 자리는 10 포함, 두번째 자리는 0 불포함
#     print(i)

# for i in reversed(range(1, 11)):
#     print(i)

# for i in range(1, 11)[::-1]:  # 슬라이싱 [시작인덱스:끝인덱스:방향]
#     print(i)

# money = 2000
# price = 1000
# coffee = 5
# for i in range(coffee):   # 0 ~ 4 
#     print("커피를 구매했습니다.")
#     money -= price     # money = money - price
#     print("남은커피 :", coffee - 1 - i)   # 4 ~ 0
#     if money < price:
#         break 

# for i in range (1, coffee + 1):  # 1 ~ 5
#     print("남은커피:", coffee - i) # 4 ~ 5
# for i in range (coffee):
#     coffee -= 1
#     print("남은커피:", coffee) # 4 ~ 0 

# prices = [500, 700, 930]
# money = int(input("돈:"))
# for i in range(len(prices)):
#     price = prices[i]
#     print(money // price)
#     print(money % price)
# 여기서 정해진 횟수는 세번 왜냐면 prices에 들어가있는 값이 3개 이기 때문이다.

# for price in prices:
#     print(money // price)
#     print(money % price)
# # for 문은 여러개로 나열되어 있는걸 한개 씩 꺼내서 for과 in 사이에서 값을 꺼낸다.
# for 문은 위처럼 사용하는게 가장 효율적이다. 
# 안에서 하나씩 꺼내서 쓰는게 목적이라면 while문 보단 for문이 효율적이다.

# for i in range(5):   #5번 반복하겠다는 뜻.
    # score = int(input("시험점수:"))
    # scores.append(score)

# for i in range(1, 10):  # 1 ~ 9
        # print("2 *", i, "=", 2*i)  # 반복문 안에 반복문을 넣어서 구구단을 완성할 수 있다.

# 이중 for문
# 2단 부터 9단 까지 구구단 완성하기
for i in range(2, 10):  # 2 ~ 9
    print(i, "단")
    for j in range(1, 10): # 1 ~ 9
        print(i, "*", j, "=", i*j)
    print(i,"--------")
# 안쪽 구문이 먼저 계산이 된다.  
