# 과제 1: [실무형] 특정 품목의 수출입 현황 보고서 준비하기

# 이 과제는 데이터 정제와 필터링 능력을 동시에 테스트합니다.
import streamlit as st
import pandas as pd
import numpy as np


# 시나리오: 여러분은 '반도체(HS코드 85)' 관련 무역 분석가입니다. 상사가 "최근 미국과 베트남의 반도체 수출 현황을 정리해달라"고 요청했습니다.

# 수행 단계:

# 전체 데이터에서 **HS코드 앞 2자리가 '85'**인 데이터만 추출하세요.

trade_data = pd.read_csv("raw_trade_data.csv", encoding="cp949")

hs_85 = trade_data[trade_data["hs_code"].astype(str).str.startswith("85")]

print(hs_85)
print("-"*60)
# 그중 **국가명이 '미국' 혹은 '베트남'**인 데이터만 필터링하세요.
USVN = hs_85[hs_85["국가명"].isin(["미국","베트남"])]
print(USVN)
print("-"*60)
# 수출금액이 없는(0인) 데이터는 분석에서 제외하세요.
No_0 = USVN[USVN["수출금액"]>0]
print(No_0)
print("-"*60)

# 결과 데이터의 상위 10개를 출력하고, semiconductor_report.csv로 저장하세요.
print(No_0.head(10))
No_0.to_csv("semiconductor_report.csv")
# 핵심 체크 포인트: * .str.startswith('85') 또는 .str[:2] == '85' 활용 능력

# isin(['미국', '베트남']) 다중 조건 필터링 이해도

print("-"*60)

# 🏆 과제 2: [데이터 클렌징] 지저분한 무역 데이터 바로잡기

# 실제 무역 데이터는 단위가 섞여 있거나 오타가 많습니다. 이를 정제하는 과제입니다.



# 시나리오: 시스템 오류로 인해 데이터의 일부가 오염되었습니다. 분석 전 데이터를 정규화해야 합니다.

# 수행 단계:

# '중량' 컬럼에 결측치가 있다면 해당 품목의 평균 중량으로 채우세요. (어려우면 0으로 채우기)
grouped_weight = trade_data.groupby("hs_code")["중량"].mean()
mean_weight = 
trade_data.loc[trade_data["중량"].isna(), "중량"] = trade_data[trade_data["중량"].isna(), grouped_weight]



print(trade_data)

print("-"*60)

# '수출입구분' 컬럼의 데이터가 영문(Import, Export)으로 되어 있다면 국문(수입, 수출)으로 일괄 변경하세요.

trade_data.loc[trade_data["수출입구분"] == "Import", "수출입구분"] = "수입"

trade_data.loc[trade_data["수출입구분"] == "Export", "수출입구분"] = "수출"

                       
print(trade_data)
print("-"*60)

# 현재 '수출금액' 단위가 '원'입니다. 이를 '백만 달러' 단위로 변환한 수출금액_M_USD 컬럼을 만드세요. (환율 1,470원 가정)
trade_data["수출금액_M_USD"] = trade_data["수출금액"] / 1470 / 1000000
print(trade_data)


# 변경 후 데이터의 각 컬럼별 데이터 타입(df.dtypes)을 확인하여 수치형 데이터가 맞는지 검증하세요.