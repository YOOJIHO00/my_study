# li_1 = ["Hello", "World", "Python"]
# # li_1의 원소를 사용하여
# # Hello World Python 이라고 출력하세요 
# print(li_1[0], li_1[1], li_1[2])

# # join(리스트)
# # 리스트의 문자열을 합친다.
# " ".join(li_1) # Hello World Python 이라고 출력된다.
# print(li_1[0] + " " + li_1[1] + " " + li_1[2]) # Hello World Python 이라고 출력된다.

# # li_1의 원소를 사용하여
# # Help 라고 출력하세요
# print(li_1[0][0:3] + li_1[2][0])    # 글자를 하나하나 뗴서 완성해도 된다.

# li_2 = [1, 2, 3]
# # li_1 과 li_2를 사용하여
# # ["Hello", "World", "Python", 1, 2, 3]
# # 을 출력하세요
# print(li_1 + li_2)
# li_1.extend(li_2)
# print(li_1)

# # li_1 과 li_2를 사용하여
# # ["Hello", 1, "World", 2, "Python", 3]
# # 을 출력하세요
# li_1.insert(1, li_2[0])
# li_1.insert(3, li_2[1])
# li_1.append(li_2[2])
# print(li_1)
"""
scores = []
scores = list()     # 두개 다 똑같은 거 (비어있는 리스트 생성)
scores.append(int(input("영어점수:")))    #함수를 여러개 호출해서 쓸 수 있음 (괄호 가장 안쪽에 있는 것 부터 실행된다.)
scores.append(int(input("국어점수")))
scores.append(int(input("수학점수")))

avg = (scores[0] + scores[1] + scores[2])/3
# sum()
# 리스트의 요소를 모두 더한다. (숫자끼리만 더할 수 있다 문자가 섞이면 에러가 난다.)
avg = sum(scorers) / 3  

if avg >= 91:
    print("A")
elif avg >= 81:
    print("B")
elif avg >= 71:
    print("C")
elif avg >= 61:
    print("D")
else:
    print("F")
"""

# 나이와 가지고 있는 돈을 입력 받는다.
# 가지고 있는 돈으로 물건을
# 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 500원이다.

age = input("나이:")
money = int( input("돈:"))
price = 500
print(money // price)
print(money % price)
 

# 나이와 가지고 있는 돈을 입력 받는다.
# 가지고 있는 돈으로 물건을
# 몇 개 살 수 있는지와 잔돈을 출력한다.
# 물건의 가격은 1번 물건 1000원
# 2번 물건 50원 3번 물건 120원이다.

age = input("나이:")
money = int(input("돈:"))
prices = [1000, 50, 120]
print(money // prices [0], money % prices [0])
print(money // prices [1], money % prices [1])
print(money // prices [2], money % prices [2])
