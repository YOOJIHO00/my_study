# 예외 처리
# 오류 발생을 잡아내서 처리하는 것

# li[1, 2, 3, 4, 5]

# li[100]

# 100/0

# f = open("없는파일", "r")

# 에러 발생 시 프로그램 중단 
# 에러 메시지를 보여준다.
# 예외 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코드
# except 블록에는 오류가 발생했을 때 수행할 코드
# try 에서 에러가 발생하지 않으면 except 블록의 코드는 실행되지 않는다.
# try:
#     100 / 0
# except:
#     print("에러발생")
# # except ZeroDivisionError as e:
#     # print(e)

# print("에러 발생 후")

# try:
#     100 / 0
# except Exception as e:  # 오류객체
#     print(e)   # e에는 에러메시지가 들어있기 때문에 에러가 나면 메시지를 출력시킨다.

# print("에러 발생 후")

# try:
#     [1, 2, 3, 4, 5] [100]
#     100 / 0
# except ZeroDivisionError as e:   # ZeroDivisionErro = 0을 잡아내는 에러(다양한 종류의 에러는 못잡는다.)
#     print(e, "0으로 나눌 수 없습니다.")
# except IndexError as e:
#     print(e, "인덱싱 할 수 없습니다.")

# print("에러 발생 후")

# finally
# 예외 발생 여부와 상관 없이 항상 수행되는 코드
# 마지막으로 수헹할 코드를 의미함
# try:
#     f = open("없는파일","r")
# except:
#     print("에러발생")
# finally:
#     f.close()

# else
# 오류가 발생하지 않으면 실행되는 코드
# try:
#     age = int(input("나이:"))
# except:
#     print("입력이 잘못되었습니다.")
#     print("숫자를 입력해주세요.")
# else:
#     if age >= 20:
#         print("성인입니다.")
#     else:
#         print("미성년자 입니다.")

class Bird:
    def fly(self):
        raise NotImplementedError   # 구현되지않은에러, 일부러 발생시킨다.
    # raise 뒤에는 에러코드가 와야 한다.
my_bird = Bird()
my_bird.fly()