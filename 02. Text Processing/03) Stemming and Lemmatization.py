from nltk import WordNetLemmatizer
from nltk import PorterStemmer
from nltk import LancasterStemmer
from nltk.tokenize import word_tokenize

lemmatizer = WordNetLemmatizer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has',
         'starting']

print("표제어 추출 전: ", words)
print("표제어 추출 후:", [lemmatizer.lemmatize(word) for word in words])

print(lemmatizer.lemmatize('dies', 'v'))
print(lemmatizer.lemmatize('watched', 'v'))
print(lemmatizer.lemmatize('has', 'v'))

stemmer = PorterStemmer()

sentence = "This was not the map we found in Billy Bones's chest, but an accurate copy, complete in all things--names " \
           "and heights and soundings--with the single exception of the red crosses and the written notes. "

tokenized_sentence = word_tokenize(sentence)

print('어간 추출 전', tokenized_sentence)
print('어간 추출 후', [stemmer.stem(word) for word in tokenized_sentence])

# NLTK Lancaster Stemmer
porter_stemmer = PorterStemmer()
lancaster_stemmer = LancasterStemmer()

words = ['policy', 'doing', 'organization', 'have', 'going', 'love', 'lives', 'fly', 'dies', 'watched', 'has',
         'starting']
print('어간추출')
print('Porter stemmer:', [porter_stemmer.stem(w) for w in words])
print('Lancaster stemmer:', [lancaster_stemmer.stem(w) for w in words])
