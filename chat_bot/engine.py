from nltk.tokenize import RegexpTokenizer, sent_tokenize, word_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string
import random
from nltk.corpus import wordnet as wn

question = "Are animals cute?"

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

def preprocessing(query):
    stop_words = set(stopwords.words('english'))
    tokenizer = RegexpTokenizer(r'\w+')
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    tokens = tokenizer.tokenize(query.lower().translate(remove_punct_dict))
    filtered_tokens = [w for w in tokens if not w in stop_words]
    ps = PorterStemmer()
    stemmed_tokens = [ps.stem(w) for w in filtered_tokens]
    lemmatizer = WordNetLemmatizer()
    tagged_tokens = pos_tag(stemmed_tokens)
    lemmatized_tokend=[]
    for word, tag in tagged_tokens:
        wntag = get_wordnet_pos(tag)
        if wntag:
            lemmatized_tokend.append(lemmatizer.lemmatize(word, pos=wntag))
        else:
            lemmatized_tokend.append(lemmatizer.lemmatize(word))

    return lemmatized_tokend

GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)
    return None


def process_request(request):
    question_tokens = preprocessing(request)
    similar_question_tokens = preprocessing("Are cats nice?")
    score, count = 0.0, 0

    return 0


def get_response(request):
    resp = greeting(request)
    return resp if resp else 'Not recognized command.'

print(process_request(question))
