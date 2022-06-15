## 01) 토큰화(Tokenization)

### keras issue
예제 구동 중 오류 발생

`from tensorflow.keras.preprocessing.text import text_to_word_sequence`

해당 패키지를 import 하는 과정에서 오류 발생

해결법: tensorflow에 관련된 패키지를 모두 제거 후 `conda` 명령어를 이용해 keras, tensorflow CPU 버전으로 설치.

### 3. 토큰화에서 고려해야할 사항
> 1) 구두점이나 특수 문자를 단순 제외해서는 안 된다.
> 2) 줄임말과 단어 내에 띄어쓰기가 있는 경우.

1번의 경우, 축약어들은 단어 사이에 구두점을 가지고 있는 경우가 있다. 따라서 구두점을 단순 제외하는 것은 도움이 되지 않는다.
또한, 달러의 경우 달러와 센트를 나누는 의미로 구두점을 활용하기도 한다. 
2번의 경우 영어권의 어퍼스트로피(')가 해당한다.

이를 해결하기 위한 표준 토큰화 예제
#### 3) 표준 토큰화 예제
> 표준으로 쓰이고 있는 토큰화 방법 중 하나인 Penn Treebank Tokenization의 규칙. <br>
> 규칙 1. 하이푼으로 구성된 단어는 하나로 유지한다. <br>
> 규칙 2. doesn't와 같이 아포스트로피로 '접어'가 함께하는 단어는 분리해준다.

샘플 문장
> Starting a **home-based** restaurant may be an ideal. it **doesn't** have a food chain or restaurant of their own.

결과에서 눈여겨 봐야 할 지점
> 'home-based', "n't",

### 4. 문장 토큰화
토큰의 단위가 문장(sentence)일 경우 단순히 마침표, 느낌표, 물음표 만으로 문장의 끝을 단정 지을 수 없다.

