# 파일 입출력
# 파이썬에서 파일 생성, 수정

# open()
# 파이썬 내장함수
# 파일을 열고, 파일 객체를 리턴한다.
# open(파일 이름, 파일 열기 모드)
# f = open("C:/Users/405/my_study/python_study/새파일.txt", 'w')  # 절대경로
# f.close()
# 파일의 경로
# 절대경로 : C:/D:/처럼 최상단 경로부터 나타낸 경로(드라이브 이름부터 나타낸 경로)
# 상대경로 : 현재 작업 위치부터 나타낸 경로

# 파일 열기 모드
# r : 읽기 모드, 파일을 읽기만 할 때 사용
# w : 쓰기 모드, 파일의 내용을 쓸 때 사용
# a : 추가 모드, 파일의 마지막에 새로운 내용을 추가할 때 사용
# \n : 줄바꿈 문자

# f = open("python_study/새파일.txt", 'w', encoding="utf-8")
# for i in range(1,11):
#     print(i, "번째 줄")
#     f.write(str(i) + "번째 줄\n")
# f.close()
# w 모드는 덮어쓰기 된다. (실행할때 마다 새 파일을 만드는 것과 동일)
# 이전 내용이 덮어쓰기 되기 때문에 주의해야한다.

# f = open("python_study/새파일.txt", 'a', encoding="utf-8")
# for i in range(11, 21):   # 11 ~ 20
#     print(i, "번째 줄")
#     f.write(str(i)+"번째 줄\n")
# f.close()

# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# readline()함수
# 첫번째 줄부터 1줄 읽어온다.
# 마우스 커서가 이동하는 것 처럼 한줄 읽어온다.
# while True:   
#     f.readline()
#     if line == " ":
#         break
#     print(line)
# f.close()

# readlines() 함수
# 파일의 모든 줄을 읽어서 리스트로 반환(줄 단위로 끊어서) 
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# lines = f.readlines()
# for line in lines:   
#     print(lines)
# f.close()

# read()함수
# 파일 내용 전체를 문자열로 리턴한다.
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# data = f.read()
# print(data)
# f.close()

# for문으로 읽기
# f = open("python_study/새파일.txt", 'r', encoding="utf-8")
# for line in f:
#     print(line)
# f.close()

# with문
# open - close 를 자동으로 해준다.
# with open("python_study/새파일", "a", encoding="utf-8") as f:
#     f.write("end of file")  # 들여쓰기 한 부분(탭 안쪽) 에 있는 부분만 출력
#     f.write("2") 
#     f.write("3") 
#     f.write("4")
# f.write("5")  # 이 부분은 실행이 안된다. (들여쓰기를 하지 않았기 때문에 파일이 이미 닫혔다.)
# 위 with문은 f.close()를 안넣어도 자동으로 닫힌다.

# csv(comma separated value)
# , 로 구분되는 값을 모아놓은 파일
# 쉼표와 탭으로 구분한다. 
# with open("python_study/data.csv", "w", encoding="utf-8")as f:
#     f.write("날짜,날씨,기온\n")
#     f.write("20230424,맑음,10\n")
#     f.write("20230425,비,0\n")

# with open("python_study/data.csv", "r", encoding="utf-8")as f:
#     data = f.readline()
#     print(data)

# 계산 결과 저장 함수
# 정수 2개를 입력받고
# 두 수를 더한 결과를 
# add_result.txt파일에
# 저장하는 함수를 정의하세요.
# 함수 이름 : add_write

# def add_write(a, b):
#     # a + b --> write
#     result = a + b
#     with open("add_result.txt", "w", "encoding=uft-8")as f:
#         f.write(str(result))

# add_write(1 , 2)

# 위 파일은 바깥쪽에 생긴다.
# 파이썬 파일에 넣고 싶으면 앞쪽에 python_study/추가 해 준다.

# 택스트 파일에 적힌 정수 2개를
# 읽어와서 더하는 함수를 정의하세요.
# 텍스트 파일 이름 : add_number.txt
# 경로 : python_study/add_number.txt
# 정수 2개를 더한 결과를 print 하세요.
# 함수 이름 : read_add_print

# def read_add_print():
#     with open("python_study/add_number.txt","r","encoding=uft-8")as f:
#         data = f.read()
#         a = int(data[0])
#         b = int(data[2])
#         print(data)

# read_add_print()