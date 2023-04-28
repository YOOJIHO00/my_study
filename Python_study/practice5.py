# 거꾸로 배열해도 같은 단어 또는 문장이 되는 
# 회문(palindrome)인지 판별하는 함수를 정의하세요.
# 함수에 문자열을 입력받고 회문이면 True
# 아니면 False를 반환하도록 정의하세요.
# 함수 이름 : is_pailndrome
# 반환값 : True 또는 False

def is_paolndrome(input_string):
    # 기러기
    # 소주 만병만 주소
    input_string = input_string.replace(" ", "")  # 문자열 중간에 있는 공백 제거
    # length = len(input_string)
    # for i in range(length//2):   # 반만 검사하는 이유 : 반이 똑같으면 나머지도 똑같기 때문이다.
    #     if input_string[i] != input_string[length -1 - i]:
    #         # 회문
    #         return False
    # return True
    return input_string == input_string[::-1]  # :: 뒤집어버리는 것 
result = is_paolndrome("소주 만병만 주소")
print(result)

# reversed("안녕하세요.")
# li1 = [1, 2, 3, 4, 5]
# li1.reverse()
# li2 = reversed(li1)
# print(li1)
# print(li2)