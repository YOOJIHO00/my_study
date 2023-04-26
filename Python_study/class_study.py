# # 객체지향(oop, object oriented programming)
# # 객체와 객체 사이의 상호작용으로 프로그램을
# # 구성하는 프로그래밍 패러다임

# # 객체지향의 특징
# # 추상화 : 공통된 속성이나 기능 도출 (주요한 특징들만 남기는 것)
# # 캡슐화 : 데이터의 구조와 연산을 결합(하나의 객체 안에 데이터와 연산이 다 들어있다.)
# # 상속 : 상위 개념의 특징이 하위 개념에 전달된다. 
# # 다형성 : 유사 객체의 사용성을 그대로 유지 (상속과 연결되는 유사한 개념)

# # 객체는 추상화와 캡슐화의 결과
# # 객체는 데이터 필드와 메소드를 가진다.

# # 클래스는 객체를 정의한 것(객체의 설계도)
# # 데이터 필드(멤버 변수, 속성)
# # 객체가 가지고 있는 변수
# # 메소드 : 객체가 가지고 있는 함수

# """
# class 클래스이름:
#     클래스 멤버 변수
#     메소드
# """
# # 클래스 이름도 변수 이름 규칙을 지켜야 한다.
# # 클래스 이름 컨벤션(관용)
# # 첫글자 대문자
# # 언더바(_) 안쓰기
# # 단어 구분 될 때 대문자   
# class Car:
#     def move(self):    # 클래스 내부에 있는 함수를 메소드라고 한다.
#         print("move")

# class SportscCar:
#     pass

# # 인스턴스 
# # 클래스를 통해 생성된 객체
# my_car = Car()   # 함수 호출하는 방법 
# my_car.move()
# # . -----> 객체 멤버 접근 연산자
# li = [1, 2, 3, 4, 5]
# li.append(6)
# # 파이썬에서는 모든게 객체다.

# # 내장함수 type()
# # 데이터의 자료형을 반환하는 함수
# print(type(li))   #class 'list'가 출력
# n = 10
# print(type(n))   # class 'int' 출력
# print(type("Hello"))  #class 'str'(문자열) 출력 

# # srt(문자열) 메소드
# # upper()
# # 모두 대문자로 변경하는 함수
# s = "Hello"
# s.upper()
# print(s.upper())
# # lower()
# # 모두 소문자로 변경
# print(s.lower())
# # strip()
# # 문자열 양쪽 끝의 특정 문자를 제거 (공백을 제거할 때 많이 사용된다.)
# s1 = "    Hello    "
# print(s1.strip())
# # lstrip(), rstrip()
# # 왼쪽, 오른쪽 끝의 특정 문자를 제거
# print(s1.lstrip)
# print(s1.rstrip)
# # split()
# # 구분자로 분할하여 리스트로 반환
# s2 = "Hello,World,Python"
# print(s2.split(','))
# # replace()
# # 문자열의 특정부분을 대체한다.
# s2.replace(',',' ')
# print(s2.replace)
# print(s2)
# s2 = s2.replace(',', ' ')
# # 파이썬에서 string객체는 수정불가능 하니까 새로운 문자를 새로 만든다.
# # "Hello" ---> "hello"
# s3 = "Hello"
# s3.lower()
# s4 = s3.replace("H", "h")
# print(s3)


# self 매개변수(파라미터)
# 모든 메소드의 첫번째 매개변수
# 메소드의 정의에는 사용되지만,
# 호출에는 사용되지 않는다.
# 객체 자신을 참조하여 클래스에 정의된
# 멤버에 접근할 때 사용한다.
# 제일 앞에 와야 한다. 무조건 첫번째 매개변수

# class Person:
#     def say(self):
#         self.name = "사람1"
#         print("Hello")
    
#     def move(self):
#         pass
    
#     def eat(self, food):
#         self.sleep()
#         print(f"{self.name}{food}를 먹었습니다.")
    
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")
# person1 = Person()
# person1.say()
# person1.eat("밥")

# initializer 초기자, 초기화기
# initialize 초기화
# refresh 의 의미 보다는 initialize의 의미로 쓰인다
# 값을 가지게 만든다 라는 뜻 (0으로 만드는거 아님)
# 변수 객체가 만들어질 때 일어난다.
# 초기화가 일어날 때 (initialize) 어떤 동작을 할지 정의 한것을 initializer라고 한다.

# class Person:
#     def __init__(self, name, age, gender, phone):
#         self.name = name
#         self.age = age
#         self.gander = gender
#         self.phone = phone
#         print("initialize")
    
#     def say_name(self):
#         print(self.name)

#     def introduce(self):
#         print(f"안녕하세요. 저는 {self.name}입니다.")
#         print(f"나이는{self.age}살이고, 성별은{self.gender}입니다.")
#         print(self.name, self.age, self.gender)

# Person 클래스에 introduce 메소드를 추가
# 이름, 나이, 성별을 print하는 메소드
# print("before")
# person2 = Person("이름", 20, "남자", "010-1234-5678")
# print("after")
# person2.say_name()
# person2.introduce()
    
# 상속 inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name     # name과 self.name은 값이 똑같은 다른 객체
#         print(f"{self.name}이 생성되었습니다.")

#     def say(self):
#         print("")

# class Dog(Animal):   # 괄호 안에 들어있는 Animal은 Animal class 를 상속 받았다는 뜻 
#     # 메소드 재정의
#     # method overriding(덮어쓰기)
#     def say(self):
#         print("멍멍")   

# my_dog = Dog("백구")  
# my_dog.say() 

# class Cat(Animal):
#     def say(self):
#         print("야옹")
        
# my_cat = Cat("나비")
# my_cat.say()

class Student:
    def __init__(self, name, age, school, grade):
        # 이름, 나이, 학교, 학년을 멤버 변수로 저장하는
        # 메소드를 만드세요
        self.name = name
        self.age = age
        self.school = school
        self.grade = grade

    def introduce(self):
        # 이름, 나이, 학교, 학년을 print하는
        # 메소드를 정의하세요.
        print(f"{self.name},{self.age},{self.school},{self.grade}")
stu1 = Student("홍길동", 20, "서울대학교", 1)
stu2 = Student("손흥민", 21, "서울대학교", 2)
stu3 = Student("류현진", 22, "서울대학교", 3)
stu_list = [stu1, stu2, stu3]
for stu in stu_list:
    stu.introduce()

