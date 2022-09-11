import re

# 정규 표현식 실습
# 1) . 기호
r = re.compile("a.c")

if r.search('kkk'):
    print('kkk 매치')
    print(r.search('kkk'))
elif r.search('abc'):
    print('abc 매치')
    print(r.search('abc'))

# 출력 결과는 아래와 같음
# <re.Match object; span=(0, 3), match='abc'>

# 2) ? 기호
r = re.compile('ab?c')

if r.search('abbc'):
    print('abbc 매치')
    print(r.search('abbc'))
elif r.search('abc'):
    print('abc 매치')
    print(r.search('abc'))

# 물음표는 있을 수도, 없을 수도 있음을 의미
# 그렇기에 ac도 매치 가능하다.
if r.search('ac'):
    print('ac 매치')
    print(r.search('ac'))

# 3) * 기호
r = re.compile('ab*c')

if r.search('a'):
    print('a 매치')
elif r.search('ac'):
    print('ac 매치')
    print(r.search('ac'))

if r.search('abc'):
    print('abc 매치')
    print(r.search('abc'))

# 별 바로 앞의 b가 0개이든, 몇 개이든 상관 없다.
if r.search('abbbbbbbbbc'):
    print('abbbbbbbbbc 매치')
    print(r.search('abbbbbbbbbc'))

# 4) + 기호


# 5) ^ 기호
# 6) {숫자} 기호
# 7) {숫자1, 숫자2} 기호
# 8) {숫자,} 기호
# 9) [] 기호
# 10) [^문자] 기호
