from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

#### 1) dictionary 사용
raw_text = 'A barber is a person. a barber is good person. ' \
           'a barber is huge person. he Knew A Secret! The Secret He Kept is huge secret. ' \
           'Huge secret. His barber kept his word. a barber kept his word. His barber kept his secret. ' \
           'But keeping and keeping such a huge secret to himself was driving the barber crazy. ' \
           'the barber went up a huge mountain.'

# 문장 토큰화
sentences = sent_tokenize(raw_text)
print(sentences)

# 토큰화된 문장을 대상으로 단어 토큰화 수행
vocab = {}
preprocessed_sentences = []
stop_words = set(stopwords.words('english'))

for sentence in sentences:
    # 단어 토큰화
    tokenized_sentence = word_tokenize(sentence)
    result = []

    for word in tokenized_sentence:
        word = word.lower() # 모든 단어를 소문자화
        if word not in stop_words: # 단어 토큰화 된 결과에 대해서 불용어를 제거
            if len(word) > 2: # 단어 길이가 2 이하인 경우에 대하여 추가로 단어를 제거
                result.append(word)
                if word not in vocab:
                    vocab[word] = 0
                vocab[word] += 1

    preprocessed_sentences.append(result)

# print(preprocessed_sentences)
# print('vocab:', vocab)

# print(vocab['barber'])

vocab_sorted = sorted(vocab.items(), key=lambda x:x[1], reverse=True)
# print(vocab_sorted)

word_to_index = {}
i = 0
for (word, frequency) in vocab_sorted:
    if frequency > 1:
        i = i + 1
        word_to_index[word] = i

# print(word_to_index)

# 상위 5개 단어만 추려내기
vocab_size = 5

words_frequency = [word for word, index in word_to_index.items() if index >= vocab_size + 1]

# 해당 단어에 대한 인덱스 정보를 삭제
for w in words_frequency:
    del word_to_index[w]

print(word_to_index)