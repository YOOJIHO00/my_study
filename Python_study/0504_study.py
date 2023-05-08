# Pandas
# 판다스

# 결측치(missimg value)
# stock.insa().sum()
# stock.isnull().sum()

# 데이터의 자료형 -> info
# stock.info()

# map
# Series의 각각의 element들을 다른 어떤 값에 대체하는 역할
# series = pd.Series([100, 200, 300])
# series
# series.map({100:"C", 200:"B", 300:"A"})
# series.map("${}".format)
# series.map("{}달러".format)
# import numpy as np
# f = lambda x : np.add(x, 3)
# series.map(f)

# def sub_custom_value(x, val):
    # return x-val
# s.apply(sub_custom_value.args=(10.))

# def add_custom_values(x, **kwargs):
    # for month in kwargs:
        # x += kwargs[month]
    # return x

# s.apply(add_custom_values, june = 30, july = 20, august = 25)

# s.apply(add_custom_values, kwargs = 30, 20, 25)

# axis 별로 apply를 적용 가능
# frame = pd.DataFrame(np.arange(12)).reshape(3, 4).columns = list("a b e d")
# frame
# frame.apply(lambda x : x.max()-x.min())
# frame.apply(lambda x : x.max() - x.min.axis = 0)   # axis = 0 : default (디폴트)
# default : 별도 설정하지 않은 "초깃값" 즉, "기본설정값"을 의미한다
# 행렬중 열을 중시한다.

# applymap
# 모든 원소에 원소별로 함수에 적용
# frame.applymap(lambda x : x ** 2)


# frame.pd.DataFrame(np.ereange(16).reahape(4, 4).index = ["r1", "r2", "r3", "r4"]columns = ["c1", "c2", "c3"], "c4])"
# frame

# frame.drop("r1")
# frame.drop("c1".axis = 1)  # KeyError : "[c1]" not found axis"
# frame1 = frame.drop("r1")
# frame.drop(columns = ["c3", "c4"])
# frame.drop("r1".inplace = True)
# inplace = 데이터가 날아감 (조심히 사용해야 한다.)

# concat
# 데이터 병합

# s1 = pd.Sreies([100, 200], index = ["c", "d"])
# s2 = pd.Series([300, 400], index = ["c", "d", "e"])
# s3 = pd.Series([500, 600], index = ["f", "g"])
# print(s1, s2, s3, sep = "WnWn")
# pd.concat([s1, s2, s3])
# pd.concat([s1, s2], axis = 1)  # SQL의 outer join(합집합)으로 돌아간다.

# Merge
# key를 이용해 데이터의 row를 기준으로 연결시켜 합치는 것과 유사하다.(SQL의 join과 유사)
# data1 = pd.DataFrame({"id" : ["01", "02", '03', "04", "05", "06"]
#                       "col1" : np.random.randint(0, 50, 6)
#                       "col2" : np.random.randint(1000, 2000, 6)})
# data1

# data2 = pd.DataFrame({"id" : ["04, "05", "06", "07"].
                            #   "col1" : np.random.randint(1000, 5000, 4)})
# data2

# inner join 
# 교집합
# pd.merge(data1, data2.on = "id")  # on은 기준
# col이 두개 있을 때 출력하면 x, y 로 구분해서 출력된다.

# outer join
# 합집합
# pd.merge(data1, data2, on = "id", how = "left")  
# how : 어떤 방식으로 병합할 것인가?{inner, outer, left, right}

# missing data

# dropna

# obj = pd.Series(["apple", "mango", np.nan, None, "peach", 1])
# obj

# frame = pd.DataFarme([[np.nan, np.nan, np.nan, np.nan]
                    #  [10, 5, 40, 6]
                    #  [5, 2, 30, 8]
                    #  [15, 3, 10, np.nan]
                    #  ].
                    #  columns = ["x1", "x2", "x3", "x4"])
# frame
# fram.dropna()
# frame.dropna(how = "all")  # how = any.all

# 결측치 채우는 방법
# fillna
# frame.fillna(0)  # method : ffill, bfill, backfill, "pad", None
# frame.fillna({"x1" : 10, "x3" : 3})
# frame.insa().sum()

# 중복제거
# duplicated() : 각 row가 중복인지(True) 아닌지(False) 알려주는 불리인 Series변환
# drop_duplicated() : duplicated를 적용한 결과가 False인 것들만 모아서 datafreme 반환

# data = pd.DataFrame({"id" : ["0001", "0002", "0003", "0001"]
                    #  "name" : ["a", "b", "c", "d"]})
# data

# data.duplicated()   # 중복체크 (True -> 중복이 되어있다.)
# data.drop_duplicated()  # 중복을 삭제


# cut
# ages = [ 20, ,35, 67, 39, 59, 44, 56, 77, 28, 80, 32, 46, 52, 19, 33, 5, 15, 50, 29, 21, 33, 48, 85, 80, 31, 10]
# bins = [0, 20, 40, 60, 100]

# cuts = pd.cut(ages, bins)
# cuts

# cuts.categories  # cut 메소드의 결과는 categoricla 이라는 특수 객체에 존재

# cuts.codes

# 구간을 균등한 길이로 나눈다.
# pd.cut(ages, 4, precision = 1).value_counts()
# precision : 소수점 자릿수, 3이면 소수점 세번째에서 반올림한다.

# 구간을 균등한 길이로 나눈다.
# pd.qcut(ages, 4).value_counts()

# get_dummies
# df = pd.DataFrame({"col1" : [10, 20, 30],
                #    "col2" : ["a", "b", "c"]})
# df
# import pandas as pd

# kbo = pd.read_csv("https://raw.githubusercontent.com/Youngpyoryu/Lecture_Note/main/%ED%8C%8C%EC%9D%B4%EC%8D%AC/kbo.csv")

# kbo.shape

# kbo.columns

# kbo["팀"].unique()

# kbo.info()

# kbo.describe()

# kbo.insa().sum()
# # kbo.isnul().sum()

# # groupby 
# # groupby를 하며 group으로 묶인 Gruopby 객체를 반환
# # 이 객체는 그룹 연산을 위해 필요한 모든 정보를 가지고 있다.
# kbo.groupby("팀").count()

# kbo. groupby(["연도", "팀"]).sum()
# kbo. groupby("팀")["승률"].max()
# kbo. groupby(["연도", "팀"])["승률", "순위"].max()

# groupby = kbo.groupby("팀")

# for name.group in grouped:
#     print(name)
#     print(group)


#     print("-" * 50)

# grouped.get_group("한화")

# import pandas as pd

# df = pd.read_csv('https://raw.githubusercontent.com/paskhaver/pandas-in-action/master/chapter_01_introducing_pandas/movies.csv')
# df


# df = pd.read_csv('https://raw.githubusercontent.com/paskhaver/pandas-in-action/master/chapter_01_introducing_pandas/movies.csv', index_col='Title')
# df

# df.head()
# df.tail()
# df.shape
# df.size

# 500번째 영화 뽑아보기.
# df.info()
# df.dtypes  # dtype보다는 info()함수가 더 좋다.

# 모두가 사랑하는 눈물없인 볼 수 없는 영화 포레스트검프의 행 값을 추출
# df.loc("Forrest Gump")

# 인덱스 레이블에는 중복이 있을 수 있다.

# df.loc["101 Dalmattians"]
# df.sort_value(by = "Year", ascending = False).head()
# df.sort_value(by = ["Studio", "Year"]).head()
# df.sort_index().head()

# 하나 이상의 기준으로 열 필터링
# df["Studio"] == "Universal"
# df[df["Studio"] == "Universal"]

# df[df["Title"] == "Forrest Gump"]

# Universal에 해당되는 2015년에 개봉한 영화를 필터링 하세요
# df["Studio"] == "Universal"
# df["Year"] == "2015"
# df[(df["Studio"] == "Universal") & (df["Year"] == 2015)]
# df[(df["Studio"] == "Universal") | (df["Year"] == 2015)]

# 1983년부터 1986년 사이에 개봉한 영화를 필터링하는 예제
# mid_80s = df["Year"].between(1983, 1986)
# df[mid_80s]

# index에서 영화 제목을 소문자로 바꾸고 
# 제목에 "dark"라는 단어가 있는 모든 영화를 찾는 예제

# has_dark_in_title = df.index.str.lower.str.contains("dark")
# df[has_dark_in_title]

# df["Gross"] = (
#    df["Gross"]
#    .str.replace("&", "", regex = False)
#    .str.replace(".", "", regex =False)
#    .astype(float)
# )

# 영화 제작사 당 총 흥행 수익을 계산하는 문제

# studios = df.groupby("Studio")
# studios["Gross"].count().sort_value(ascending = False).head()
# studios["Gross"].sum().head()
# studios["Gross"].sum().sort_value(ascending = False).head()

# import matplotlib.pyplot as plt
# %matplotlib notebook #jupyter notebook에서 그려주세요.
# %matplotlib qt #별도의 팝업창에서 그래프 출력(colab X)
# 그래프 위 문자들은 메모리 주소 이다.

# 바깥이 피겨 안쪽이 엑시스


# import matplotlib.pyplot as plt
# %matplotlib notebook #jupyter notebook에서 그려주세요.
# # %matplotlib qt #별도의 팝업창에서 그래프 출력(colab X)
# # 그래프 윗 부분에 문자들은 메모리주소


# xlim, ylim
# x축의 길이와 y축의 길이 조정

# x = np.arange(10)
# y = x + 10
 
# plt.plot(x, y)
# plt.show
# plt.xlim([0, 10])
# plt.ylim(0, 20)
# plt.plot(x, y)

# x = np.arange(-np.pi.np.pi,0.02)
# y1 = np.sin(x)
# y2 = np.cos(x)

# plt.plot(x, y1, lable = "sin", color = (0, 1, 0, 3, 0, 5)
# plt.plot(x, y2.lable = "cos", color = "r")
# plt.legend()
# plt.show()

# x = np.arange(10)
# y1 = x
# y2 = x**2 -x

# fig,axs = plt.subplots(2,1) #2행 1열로 그리겠습니다.
# fig.set_facecolor('#c79fef') #뒤의 배경

# axs[0].plot(x,y1) #첫번째 행
# axs[1].plot(x,y2) #두번째 행

# axs[0].set_facecolor('pink') #첫번째 행의 배경
# axs[1].set_facecolor('skyblue') # 두번째 행의 배경

# plt.show()

# x = np.arange(-5, 5, 0, 5)
# y1 = x 
# y2 = x ** 2
# y3 = np.sin(x)
# y4 = np.cos(x)

# plt.plot(x, y1)
# plt.plot(x, y2, maker = "D")
# plt.plot(x, y3, color = "r")
# plt.plot(x, y4, linestyle = "dashed")
# plt.show()

# data = {"사과" : 21, "바나나" : 15, "배" : 5, "키위" : 20}
# names = list(data.keys())
# values = list(data.values())

# fig.ax = plt.subplots
# ax.bar(names.values)

# data = np.random.rand(10000)
# fix.ax = plt.subplots()
# ax.hist(data.bins = 100, facecolor = "r")
# plt.show()

# n = 50
# x = np.random.rand(n)
# y = np.random,rand(n)

# plt.scatter(x, y)
# plt.show()