# import kss
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize
from nltk.tag import pos_tag
from tensorflow.keras.preprocessing.text import text_to_word_sequence

from konlpy.tag import Okt
from konlpy.tag import Kkma

print('단어 토큰화1 :',word_tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
print('단어 토큰화2 :',WordPunctTokenizer().tokenize("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))
print('단어 토큰화3 :',text_to_word_sequence("Don't be fooled by the dark sounding name, Mr. Jone's Orphanage is as cheery as cheery goes for a pastry shop."))

# 3. 3) 표준 토큰화 예제
sample_text = "Starting a home-based restaurant may be an ideal. it doesn't have a food chain or restaurant of their own."
tokenizer = TreebankWordTokenizer()

print('트리뱅크 워드 토크나이저: ', tokenizer.tokenize(sample_text))

# 4. 문장 토큰화
sample_sentence = "His barber kept his word. But keeping such a huge secret to himself was driving him crazy. Finally, " \
              "the barber went up a mountain and almost to the edge of a cliff. He dug a hole in the midst of some " \
              "reeds. He looked about, to make sure no one was near. "

print('문장 토큰화 1:', sent_tokenize(sample_sentence))

sample_sentence2 = "I am actively looking for Ph.D. students. and you are a Ph.D student."

print('문장 토큰화 2:', sent_tokenize(sample_sentence2))

# KSS를 활용한 한국어 문장 토큰화
kss_sample = '딥 러닝 자연어 처리가 재미있기는 합니다. 그런데 문제는 영어보다 한국어로 할 때 너무 어렵습니다. 이제 해보면 알걸요?'
# kss 실행 부분에서 오류 발생. 넘어간다
# concurrent.futures.process.BrokenProcessPool: A process in the process pool was terminated abruptly while the future was running or pending.
# print(kss.split_sentences(kss_sample))

# 7. NLTK와 KoNLPy를 이용한 영어, 한국어 토큰화 실습
token_sample = "I am actively looking for Ph.D. students. and you are a Ph.D. student."
tokenized_sentence = word_tokenize(token_sample)
print('단어 토큰화: ', tokenized_sentence)
print('품사 태깅: ', pos_tag(tokenized_sentence))

print("\nKoNLPy 패키지의 Okt, Kkm 형태소 분석기를 이용한 한국어 토큰화")
sample_ko_token = "열심히 코딩한 당신, 연휴에는 여행을 가봐요"

okt = Okt()

print('OKT 형태소 분석:', okt.morphs(sample_ko_token))
print('OKT 품사 태깅:', okt.pos(sample_ko_token))
print('OKT 명사 추출:', okt.nouns(sample_ko_token))

kkma = Kkma()

print('꼬꼬마 형태소 분석:', kkma.morphs(sample_ko_token))
print('꼬꼬마 품사 태깅:', kkma.pos(sample_ko_token))
print('꼬꼬마 명사 추출:', kkma.nouns(sample_ko_token))

