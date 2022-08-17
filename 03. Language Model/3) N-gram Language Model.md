## 3) N-gram 언어 모델
> n-gram 언어 모델은 여전히 카운트에 기반한 통계적 접근을 사용하고 있으므로 SLM의 일종
> 
> 이전에 등장한 모든 단어를 고려하는 것이 아니라 일부 단어만 고려하는 접근 방법을 사용
> 
> 이때 일부 단어를 몇 개 보느냐를 결정하는데 이것이 **n-gram에서의 n이 가지는 의미**

통계적인 방법은 맞는데, 일부 단어만 고려해서 접근하는 방식을 채택하고 있다는 뜻.

### 1. 코퍼스에서 카운트하지 못하는 경우의 감소
앞선 SLM 챕터에서도 확인했다시피 연구자가 확보해 놓은 코퍼스에 "계산하고 싶은 문장이나 단어가 없을 수 있다는 점"이 문제다.

또한, 문장의 길이가 길어질수록 이런 문제는 심각해진다. 따라서 "참고하는 단어들을 줄이면 카운트를 할 수 있을 가능성을 높"일수 있다.

``P(is|An Adorable little boy) ≈ P(is|Boy)``

여기서 물결 등호는 "거의 같다"라는 의미로, "almost equal to"라고 이해하면 쉽다. 동양권에서는 같은 의미의 기호로 ≒를 더 많이 사용한다.
[equal vs almost equal](https://allcalc.org/14969)

아무튼 An...으로 시작하는 문장을 통째로 조건하 확률 식에 넣기 보다, 사실상 같은 의미라고 할 수 있는 Boy만을 조건하 확률에 활용한다.
즉, "boy is라는 더 짧은 단어 시퀀스가 존재할 가능성이 더 높"다는 것이다.

교재에서는 위의 사례가 "지나친 일반화"로 느껴질 경우, ``P(is|little boy)`` 정도로 생각해보는 것을 권장하고 있다.

이로써 내가 "갖고 있는 코퍼스에서 해당 단어의 시퀀스를 카운트 할 확률이 높"아진다.

### 2. N-gram
> n-gram은 n개의 연속적인 단어 나열을 의미
> 
> 갖고 있는 코퍼스에서 n개의 단어 뭉치 단위로 끊어서 이를 하나의 토큰으로 간주

따라서 예시를 들어보면 다음과 같다. 샘플 문장은 위와 동일.

> An adorable little boy is spreading smiles

> unigrams : an, adorable, little, boy, is, spreading, smiles
> 
> bigrams : an adorable, adorable little, little boy, boy is, is spreading, spreading smiles
> 
> trigrams : an adorable little, adorable little boy, little boy is, boy is spreading, is spreading smiles
> 
> 4-grams : an adorable little boy, adorable little boy is, little boy is spreading, boy is spreading smiles

이렇듯 n에 따라서 명칭이 달라지는 것을 확인할 수 있다. 가령 n=4라고 가정해보자.
그렇다면 위 문장의 "spreading" 뒤에 올 단어를 예측하기 위해서는 앞의 3개의 단어만(n-1)을 고려한다.

``P(w|boy is spreading) = count(boy is spreading w) / count(boy is spreading)``

위와 같은 식을 사용할 수 있는데, 여기서 생각해보아야 할 것이 있다.

가지고 있는 코퍼스에서 boy is spreading가 1,000번 등장했다고 가정한다.
그리고 "boy is spreading insults가 500번 등장"하고, "boy is spreading smiles가 200번 등장"했다고 가정하자.
그렇다면 확률상 모욕하다라는 뜻인 insults가 옳은 결과라고 판단하게 된다.

insults: ``500 / 1000 = 50%``
smiles: ``200 / 1000 = 20``

### 3. N-gram Language Model의 한계
