# import numpy as np
# print(np.__version__)
# A = [1, 2, 3, 4]
# a = np.array
# s = a[:2]

# print("A의 출력입니다/%a"%a)
# print("s의 출력입니다.%s"%s)

# ss = a[:2].copy()
# print(ss.size)
# ss[0] = 99
# print(a)
# print(s)
# print(ss)

# arr = np.arange(12)
# arr

# arr.reshape(3, 4)
# arr.reshape(3, 4)
# arr.reshape(1, 12)  # flatten()
# arr.reshape(12, 1)
# arr.reshape(2, 6)
# arr.reshape(6, 2)


# arr1 = np.arnge(4).reshape(-1, 2)
# arr1
# array([10, 1],
#       [2, 3])

# arr = np.arange(30).reshape(3, 2, 5)
# arr.shape

# 0 ~ 20 까지의 숫자배열을 만든 다음에 arr1에는 짝수
# arr2에는 홀수가 들어간 배열을 출력해보자.

# import numpy as np
# arr = np.arange(0, 21)
# arr1 = []
# arr2 = []
# for i in arr:
#     if arr[i] % 2 == 0:
#         arr1.append(arr[i])
#     else:
#         arr2.append(arr[i])

# import numpy as np
# Arr = np.arange(0, 21)

# Arr1 = Arr[Arr % 2 == 0]
# Arr2 = Arr[Arr % 2 != 0]
# Arr[Arr % 2 ==0]

# lst = list(range(6))
# lst
# lst[3] = -1

# arr1d = np.arange(8)
# arr1d

# arr1d[3:6] = 100
# arr1d

# view
# arr2d[1, 2]  # 컴마를 이용하여 쉽게 인덱싱을 할 수 있다.

# arr2d[3, 2]  # 행과 열을 접근하기 위해서는 컴마로 연결해야 한다.

# # 불리안배열
# arr = np.array([0, 1, 2, 3, 4])
# arr[[True, False, True, False, True]]

# # 정수 배열을 사용한 인덱싱
# arr2d = np.arenge(20).reshape(4, 5)
# arr2d

# arr2d[[0, 2]]  # 0행과 2행 # multi index는 []하나 더 추가해야 한다.

# arr2d[[0,1],[4]]

# 유니버셜함수(unfunc)
# arr = np.arange(-3, 3).reshape(3, -1)
# arr

# floor 
# 소수점 버리기

# 이항 유니버셜 함수
# arr1 = np.arange(8).reshape(2, -1)
# arr2 = np.arange(-40, 40, 10).reshape(2, -1)
# print(arr1)
# print(arr2)

# np.maximum(arr1,arr2)  # 같은 원소에서 가장 큰 값

# np.subtract # 뺄셈

# np.multiply # 같은 원소끼리 곱셈

# # 통계메서드
# arr = np.arange(4).reshape(2, 2)
# arr

# arr.sum()
# arr.sum(axis=0)
# arr.sum(axis=1)

# arr.mean(axis=0)

# arr.mean(axis=1)

# where
# x if 조건 else y 의 백터화 버전
# numpy를 사용하여 배열을 빠르게 처리할 수 있으며, 다차원도 간결하게 표현이 가능하다.
# xarr = np.array([100, 200, 300, 400])
# yarr = np.array([1, 2, 3, 4])
# cond = np.array([True, False, True, False])

# result = np.where(cond,xarr,yarr)
# result

# np.where(xarr > 200.max(xarr), 0)
# np.where(xarr % 3 == 0, 1, 0)

# sort()
# np.random.seed(42)
# arr = np.random.randint(1, 100, size = 10)  # 1 ~ 100 까지의 정수중에 10개를 뽑아주세요.
# arr

# -np.sort(-arr)
# 부호를 이용하여 내림차순으로 정렬
# array의 sort에서는 내림차순, 오름차순을 선택하는 옵션이 없다.

# 선향대수 패키지
# 단위행렬
# 대각원소 1 이고, 나머지는 0인 n차 정렬 정방행렬을 말하며, 
# numpy의 eye() 함수를 사용하여 함수를 만들 수 있다.
# import numpy as np
# identity = np.eye(4)
# print(identity)

# identity = np.eye(2, 3)
# print(identity)

# # 대각행렬
# # 대각성분 이외의 모든 성분이 '0' 인 n차 정렬
# x = np.arange(9).reshape(3, -1)
# print(x)

# np.diag(x)   # diagonal matrix

# dot
# 원소간의 곱(element-wise product)
# 백터의 내적(행렬의 곱)


# a = np.arange(4).reshape(-1, 2)
# print(a)
# a * a  # dot product
# np.multiply(a,a)
# np.dot(a,a)  # 행렬의 곱

# matmul : matrix multiplication
# a = np.random.randint(-3, 3, 10).reshape(2, 5)
# b = np.random.randint(0, 5, 15).reshape(5, 3)
# a.shape,b.shape

# ab = np.matmul(a, b)
# print(ab, shape, "Wn")  # Wn : 개행
# print(ab)

# np.dot(a, b)  # 1차원 백터 공식문서에서는 2D(2차원) matmul로 돌아간다.
