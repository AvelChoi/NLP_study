import re

# 불필요한 단어 제거 실습
text = "I was wondering if anyone out there could enlighten me on this car."

# 길이가 1~2인 단어, 정규표현식 이용 제거
shortword = re.compile(r'\W*\b\w{1,2}\b')
print(shortword.sub('', text))

# 결과
#  was wondering anyone out there could enlighten this car.
