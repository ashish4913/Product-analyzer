import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import TweetTokenizer
import preprocessor as p
list1=["good","bad","not satisfied"]
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
classified_review=[]
for i in list1:
        message=i
        data = [message]
        show= clean(message)		
        show=re.sub(r'[0-9]+','',show)
        show=re.sub(r'[^\w\s]','',show)
        show = show.lower()
        show = show.split()
        show = [lemmatizer.lemmatize(word) for word in show if not word in stopwords.words('english')]
        show = ' '.join(show)
        vect = cv.transform([show]).toarray()
        my_prediction = clf.predict(vect)
        classified_review.append(int((my_prediction.tolist())[0]))
print(classified_review)