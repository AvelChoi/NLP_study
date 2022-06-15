# import kss
from nltk.tokenize import word_tokenize
from nltk.tokenize import WordPunctTokenizer
from nltk.tokenize import TreebankWordTokenizer
from nltk.tokenize import sent_tokenize
from tensorflow.keras.preprocessing.text import text_to_word_sequence

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

