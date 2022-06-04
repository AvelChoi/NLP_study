import pandas as pd
import numpy

# 1) 시리즈
sr = pd.Series([17000, 18000, 1000, 5000],
               index=["피자", "치킨", "콜라", "맥주"])

print(f'시리즈 출력 \n{sr}')

print(f'시리즈의 값: {format(sr.values)}')
print(f'시리즈의 인덱스: {format(sr.values)}')

# 2) 데이터 프레임
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
index = ['one', 'two', 'three']
columns = ['A', 'B', 'C']

df = pd.DataFrame(values, index=index, columns=columns)
print(df)

# 3) 데이터 프레임의 생성
data = [
    ['1000', 'Steve', 90.72],
    ['1001', 'James', 78.09],
    ['1002', 'Doyeon', 98.43],
    ['1003', 'Jane', 64.19],
    ['1004', 'Pilwoong', 81.30],
    ['1005', 'Tony', 99.14],
]

# 리스트로부터 df 생성 가능
df = pd.DataFrame(data)
print(df)

df = pd.DataFrame(data, columns=['학번', '이름', '점수'])
print(df)

# 딕셔너리도 물론 가능
data = {
    '학번': ['1000', '1001', '1002', '1003', '1004', '1005'],
    '이름': ['Steve', 'James', 'Doyeon', 'Jane', 'Pilwoong', 'Tony'],
    '점수': [90.72, 78.09, 98.43, 64.19, 81.30, 99.14]
}

df = pd.DataFrame(data)
print(df)

# 4) 데이터 프레임 조회하기
print(df.head(3))  # 앞의 3개만 조회 가능
print(df.tail(3))
print(df['학번'])

# 5) 외부 데이터 읽기

