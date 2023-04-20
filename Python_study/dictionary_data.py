# dictionary(딕셔너리) 자료형
# key-value 형태
# key : value
# # 여러가지 자료 파일에 구애받지 않고 사용 가능
# person = {"이름" : "이름", "나이" : 18, "점수" :{"영어" : 80, "국어" : 90, "수학": 100 } }

# print(person["나이"])
# print(person["점수"]["영어"])

# dict_1 = {1 : 'a'}
# dict_1['b'] = 2    # 'b' : 2 key - value 쌍 추가 
# dict_1 [1] = 'c'
# del dict_1[1]
# print(dict_1)

dict_2 = {1:'a', 2:'b', 3:'c'}
# 딕셔너리에서 key 값만 리스트 형태로 돌려준다.
dict_keys = dict_2.keys()
print(dict_keys)

# value()
# 딕셔너리에서 value 값만 리스트 형태로 돌려준다.
dict_values = dict.values()
print(dict_values)

# items()
# 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
dict_items = dict_2.items()
print(dict_items)

# get(key)
# 키에 대응되는 value를 돌려준다.
# key값이 존재하지 않으면 None을 돌려준다.
# dict_2.get["나이"]
print(dict_2.get("나이"))
print(dict_2.get("나이", "나이불명"))

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
# 아무것도 안남기고 싹 다 비운다.
dict_2.clear()
print(dict_2)
