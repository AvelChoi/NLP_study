import pandas as pd
import pandas_profiling

data = pd.read_csv('spam.csv', encoding='latin1')

# print(data[:5])

# 리포트 생성
pr = data.profile_report()

# 리포트 살펴보기
pr.to_file('./pr_report.html')
