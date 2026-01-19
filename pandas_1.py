import pandas as pd
import numpy as np

dict_data = {"a":1, "b":2, "c":3}
series_data = pd.Series(dict_data)
print(type(series_data))
print(series_data)


list_data = ["2026-1-19", 3.14, "abc" , 100, True]
series_data = pd.Series(list_data)
print(type(series_data))
print(series_data)

dict_date = {"c0":[1,2,3], "c1":[4,5,6], "c2":[7,8,9], "c3":[10,11,12], "c4":[13,14,15]}
df = pd.DataFrame(dict_date)
print(type(df))
print(df)

print("-"*30)

# pandas 데이터내용 확인
# .columns  컬럼명 확인
# .head() 상위 5개 데이터 확인
# .tail() 하위 5개 데이터 확인
# .shape (행, 열)데이터 크기 확인
# .info() 데이터프레임 요약정보 확인
# .type() 데이터 타입 확인

# 파일 불러오기
# 형식       읽기          쓰기
# csv     read_csv      to_csv
# excel   read_excel    to_excel
# json    read_json     to_json
# html    read_html     to_html


# ./ = 현재 위치에서 하위폴더로 접근
# ../ = 현재 위치에서 상위폴더로 접근

titaniic = pd.read_csv("Titanic-Dataset.csv")
print(titaniic.columns)
print(titaniic.head())
print(titaniic.tail(10))
print(titaniic.shape)
print(titaniic.info())
print(type(titaniic))

print("-"*30)

# pandas 에서 특정 열을 선택
# 열 1개 선택 = Series 객체 반환
# 데이터프레임의 열 데이터 1개만 선택할 때 2가지 방법
# 1) 대괄호 [] 안에 열 이름을 따옴표로 함께 입력
# 2) 점 . 다음에 열 이름을 입력

# 열 n 개 선택 = DataFrame 객체 반환
# 1) 대괄호 [] 안에 열 이름을 리스트로 입력 = 대괄호 안에 리스트
# *** 만약에 열 1개를 데이터프레임 객체로 추출하려면 열 이름을 리스트로 입력 ***

names = titaniic["Name"]
print(names.head())

names = titaniic.Name
print(names.head())
print(type(names))
print(names.shape)

double_column = titaniic[["Sex", "Age"]]
print(double_column.head())
print(type(double_column))
print(double_column.shape)

# pandas 데이터 필터링

# 1. boolean 인덱싱 = True 값을 가진 행만 추출
# 2. .isin() = 각각의 요소가 데이터프레임 또는 시리즈에 존재하는 파악한 후 T/F 로 반환
# 3. .isna() = 결측값은 True, 결측값이 아니면 False 로 반환
# 4. .notna() = 결측값이 아니면 True, 결측값이면 False 로 반환

print(double_column["Age"] > 35) # 각 행에 대해 True/False 반환

above_35 = double_column[double_column["Age"] >= 35]  # True 값만 추출
print(above_35.head()) #True 값만 추출된 데이터프레임 출력

# 성별이 남자인것만 추출
male = double_column[double_column["Sex"] == "male"]
print(male.head())

# Pclass 가 1등급인 승객만 추출
print(titaniic.head())
Pclass_1 = titaniic[titaniic["Pclass"].isin([1])]
print(Pclass_1.head())

print("-"*30)
# Age 가 20~40 사이인 승객만 추출
print(double_column.head())
age2040 = double_column[(double_column["Age"].isin(np.arange(20,41)))]
print(age2040.head())
print("-"*30)

# Age 가 결측치인 승객만 추출
print(double_column.head(7))
class_2 = double_column["Age"].isna()
print(class_2.head(7))


# Age 가 결측치가 아닌 승객만 추출
class_3 = double_column["Age"].notna()
print(class_3.head(7))

print("-"*30)

# 결측값 처리 방법
# 행제거

print(double_column.head(10))

age5 = double_column[double_column["Age"].notna()]
print(age5.head(10))

# 결측값 제거
# .dropna(axis=0)  = 결측값들이 들어있는 행 전체 삭제
# .dropna(axis=1)  = 결측값들이 들어있는 열 전체 삭제

print(titaniic.head()) # 원본 데이터프레임 출력
print(titaniic.dropna()) # 결측값이 포함된 행 전체 삭제
print(titaniic.dropna(axis=1)) # 결측값이 포함된 열 전체 삭제

# pandas 이름과 인덱스로 특정 행과 열 선택
# .loc[]  = 행 이름과 열 이름으로 인덱싱 : DataFrame객체.loc[행이름, 열이름]
# .iloc[] = 행 번호와 열 번호로 인덱싱 : DataFrame객체.iloc[행번호, 열번호]

name35 = titaniic.loc[titaniic["Age"] >=35, ["Name", "Age"]]
print(name35.head())

name35.iloc[[1,2,3],0] = "No name"
print(name35.head())

# pandas 데이터 통계
# .mean() = 평균
# .median() = 중앙값
# .describe() = 다양한 통계량 요약 (count, mean, std, min, 25%, 50%, 75%, max)
# .agg() = 여러개의 열에 다양한 함수 적용 (각 열에 대해 다른 함수 적용 가능) 
# : group.객체.agg
# 모든열에 여러 함수를 매핑 : group.객체.agg([함수1, 함수2, ...])
# 각 열마다 다른 함수 매핑 : group.객체.agg({"열1": 함수1, "열2": 함수2, ...})
# .groupby() = 특정 열을 기준으로 그룹화하여 통계량 산출
# .value_counts() = 특정 열의 고유값별 빈도수 계산

print("----평균 나이----")
print(titaniic["Age"].mean()) # Age 열의 평균

print("----중앙값----")
print(titaniic["Age"].median()) # Age 열의 중앙값

print("----기본 통계량----")
print(titaniic.describe()) # 기본 통계량 출력

print("----나이와 요금의 평균 및 표준편차----")
print(titaniic[["Age","Fare"]].agg(["mean", "std"]))

print("----열 별 사용자 집계----")
agg_dict = {"Age": ["min", "max", "mean"],
            "Fare": ["median", "sum"]}
print(titaniic.agg(agg_dict))

print("----성별 기준으로 평균 나이 및 요금----")
grouped_sex = titaniic.groupby("Sex")
print(grouped_sex[["Age","Fare"]].mean())

print("----객실 등급별(Pclass) 인원수----")
print(titaniic["Pclass"].value_counts())


print("----성별 인원수----")
print(titaniic["Sex"].value_counts())

print("----새로운 열(country)을 USA로 생성----")
titaniic["Country"] = "USA"
print(titaniic)

print("----기존의 열을 계산해서 새로운 열을 추가----")
titaniic["New_age"] = titaniic["Age"]+10
print(titaniic)

# 나이가 20세 미만이면 child, 아니면 adult
print("----기존의 열을 계산해서 새로운 열을 추가----")
titaniic["Age_group"] = "Adult" # 열의 모든 데이터를 "Adult"로 저장
titaniic.loc[titaniic["Age"]<20,"Age_group"] = "Child"  # 열의 데이터 중에 20미만인 데이터를 모두 "Child"로 저장
print(titaniic)

print("현재 열의 개수:", len(titaniic.columns))
print("현재 열의 목록:", titaniic.columns)
# 데이터 프레임에 가장 마지막 인덱스 행 추가
new_index = len(titaniic)
print(new_index)
print(titaniic.tail())

titaniic.loc[new_index] = [996, 1, 3, "Tony Choi", "male", 27, 0,0,"Pc123",100.0,"C123","S","USA",63,"Adult"]

new_data = pd.DataFrame({
    "Name":["Alice", "Bob"],
    "Age" : [22,30],
    "Sex" : ["female","male"],
    "Survived" : [1,0]
})

titaniic = pd.concat([titaniic,new_data], ignore_index=True)

print(titaniic.tail())

# titaniic["Name"].str.startswith("Sa") = 문자열이 데이터가 Sa 로 시작하는 자료
# titaniic[titaniic["Age"].astype(str).str.startswith("2")] = 숫자열을 문자열로 전환 후 2로 시작하는 자료 

# 파일 저장
# titaniic.to_csv("", ignore_index=True)
# titaniic.to_excel("")
