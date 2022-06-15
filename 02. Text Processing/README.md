# 01) 토큰화(Tokenization)

## keras issue
예제 구동 중 오류 발생

`from tensorflow.keras.preprocessing.text import text_to_word_sequence`

해당 패키지를 import 하는 과정에서 오류 발생

해결법: tensorflow에 관련된 패키지를 모두 제거 후 `conda` 명령어를 이용해 keras, tensorflow CPU 버전으로 설치.

## 3. 토큰화에서 고려해야할 사항
> 1) 구두점이나 특수 문자를 단순 제외해서는 안 된다.
> 2) 줄임말과 단어 내에 띄어쓰기가 있는 경우.

1번의 경우, 축약어들은 단어 사이에 구두점을 가지고 있는 경우가 있다. 따라서 구두점을 단순 제외하는 것은 도움이 되지 않는다.
또한, 달러의 경우 달러와 센트를 나누는 의미로 구두점을 활용하기도 한다. 
2번의 경우 영어권의 어퍼스트로피(')가 해당한다.

이를 해결하기 위한 표준 토큰화 예제
### 3) 표준 토큰화 예제
`tokenizer = TreebankWordTokenizer()` `tokenizer.tokenize(sample_text))`

> 표준으로 쓰이고 있는 토큰화 방법 중 하나인 Penn Treebank Tokenization의 규칙. <br>
> 규칙 1. 하이푼으로 구성된 단어는 하나로 유지한다. <br>
> 규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다.

샘플 문장
> Starting a **home-based** restaurant may be an ideal. it **doesn't** have a food chain or restaurant of their own.

결과에서 눈여겨 봐야 할 지점
> 'home-based', "n't",

## 4. 문장 토큰화
`sent_tokenize(sample_sentence)`

토큰의 단위가 문장(sentence)일 경우 단순히 마침표, 느낌표, 물음표 만으로 문장의 끝을 단정 지을 수 없다.

NLTK에서는 영어 문장의 토큰화를 수행하는 sent_tokenize를 지원.
첫 번째 샘플 문장은 마침표가 문장 사이에 없는 상태였기에 문제 없이 문장 토큰화 성공.
두 번째 샘플 문장은 Ph.D 등 보다 토큰화에 까다로운 요소가 있다.

> I am actively looking for Ph.D. students. and you are a Ph.D student.

실행 결과: ['I am actively looking for Ph.D. students.', 'and you are a Ph.D student.']
 
한국어에 대한 문장 토큰화 도구 또한 존재: KSS(Korean Sentence Splitter) `pip install kss`

## 5. 한국어에서의 토큰화의 어려움
> 하지만 한국어는 영어와는 달리 띄어쓰기만으로는 토큰화를 하기에 부족합니다. <br>
> 한국어의 경우에는 띄어쓰기 단위가 되는 단위를 '어절'이라고 하는데 어절 토큰화는 한국어 NLP에서 지양 <br>
> 한국어는 어절이 독립적인 단어로 구성되는 것이 아니라 조사 등의 무언가가 붙어있는 경우가 많아서 이를 전부 분리해줘야 한다는 의미

인턴을 하면서도 들었던 이야기지만, 한국어는 영어와 달리 띄어쓰기만으로는 제대로 된 의미 파악이 어렵다.
그래서 영어권의 업체들이 가져온 자연어 처리 솔루션이 막상 예상했던 것 만큼 결과가 나오지 않았던 사실도 함께 배울 수 있었다.

따라서
> 한국어 토큰화에서는 형태소(morpheme) 란 개념을 반드시 이해해야 합니다. <br>
> 형태소(morpheme)란 뜻을 가진 가장 작은 말의 단위를 말합니다. <br>
> 이 형태소에는 두 가지 형태소가 있는데 자립 형태소와 의존 형태소입니다.

