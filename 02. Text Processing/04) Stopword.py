from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt

# NLTK에서 불용어 확인하기
# 이건 뭐 별다른걸 하는건 아니고 그냥 NLTK에 불용어가 몇 개 있나 확인해본다.
stop_words_list = stopwords.words('english')
print('불용어 개수:', len(stop_words_list))
print('불용어 10개 출력:', stop_words_list[:10])
