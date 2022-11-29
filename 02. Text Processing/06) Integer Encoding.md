## 06) 정수 인코딩(Integer Encoding)
컴퓨터는 당연히 문자보다 숫자를 더 잘 처리하는데, 
자연어처리에서는 이런 이점을 활용하기 위해 텍스트를 숫자로 바꾸는 여러가지 기법들이 있다.

특히 이번 단원에서는 첫 단계로 **각 단어를 고유한 정수에 맵핑(mapping)** 시키는 전처리 작업에 대해 다룬다.

> 갖고 있는 텍스트에 단어가 5,000개
> 1번부터 5,000번까지 단어와 맵핑되는 고유한 정수, 다른 표현으로는 인덱스를 부여

또한, 이러한 인덱스는 단어 등장 빈도수를 기준으로 정렬하여 부여하는 것이 일반적이다.

### 1. 정수 인코딩(Integer Encoding)
앞서 설명한대로, 단어를 빈도수 순으로 정렬한 단어 집합(vocabulary)를 만든다.
이후 빈도수가 높은 순서대로 차례로 인덱스를 부여하는 방법이 있다.

#### 1) dictionary 사용
```python
from nltk.tokenize import sent_tokenize
raw_text = "A barber is a person. a barber is good person. a barber is huge person... (중략)"
sentences = sent_tokenize(raw_text)
print(sentences)
```
결과
> ['A barber is a person.', 'a barber is good person.', 'a barber is huge person.', 'he Knew A Secret!', 
> 'The Secret He Kept is huge secret.', 
> 'Huge secret.', 'His barber kept his word.', 'a barber kept his word.', 'His barber kept his secret.', 
> 'But keeping and keeping such a huge secret to himself was driving the barber crazy.', 'the barber went up a huge mountain.']

우선 앞서 했던 실습과 동일한 내용. 문장 단위로 토크나이징 된 것을 확인할 수 있다.
이제 **정제 작업과 정규화 작업을 병행, 단어 토큰화를 수행**한다.

본 예제의 처리 방식
* 단어들을 소문자화
* 단어의 개수를 통일
* 불용어와 단어 길이가 2 이하인 경우에 대해서 단어 일부 제외

"텍스트를 수치화하는 단계라는 것은 본격적으로 자연어 처리 작업에 들어간다는 의미"이므로
"단어가 텍스트일 때만 할 수 잆는 최대한의 전처리를 끝내 놓아야"한다.

> [['barber', 'person']
> , ['barber', 'good', 'person']
> , ['barber', 'huge', 'person']
> , ['knew', 'secret']
> , ['secret', 'kept', 'huge', 'secret']
> , ['huge', 'secret']
> , ['barber', 'kept', 'word']
> , ['barber', 'kept', 'word']
> , ['barber', 'kept', 'secret']
> , ['keeping', 'keeping', 'huge', 'secret', 'driving', 'barber', 'crazy']
> , ['barber', 'went', 'huge', 'mountain']]

preprocessed_sentences는 위와 같이 나왔다. 한편, vocab은 아래와 같다. 단어 단위로 토큰화를 거치며 소문자로 모두 바꾸어 놓았고,
각 단어별 빈도수 순으로 정렬된 것을 확인할 수 있다.
```python
vocab: {'barber': 8, 'person': 3, 'good': 1, 'huge': 5, 'knew': 1, 'secret': 6, 'kept': 4, 'word': 2, 'keeping': 2 , 'driving': 1, 'crazy': 1, 'went': 1, 'mountain': 1}

print(vocab['barber'])
```
이제 파이썬~~으로 코테 볼 때마다 뭐드라 하는~~ 딕셔너리의 기능을 활용해, 단어를 통해 빈도수를 찾을 수 있다. 값으로 당연히 8이 나온다.

딕셔너리는 키-값으로 이루어져 있고, 이를 정렬하기 위해서는 람다식을 활용해야 한다. 코드는 다음과 같다.
```python
vocab_sorted = sorted(vocab.items(), key=lambda x:x[1], reverse=True)
```

이렇게 정렬은 했지만, 결국 최종적으로 순위를 1부터 부여하고자 한다.